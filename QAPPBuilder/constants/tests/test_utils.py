# test_utils.py
# !/usr/bin/env python3
# coding=utf-8

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from django.http import HttpResponse
from io import BytesIO
from zipfile import ZipFile
import os
import tempfile

from constants.utils import (
    get_attachment_storage_path,
    split_email_list,
    is_epa_email,
    non_epa_email_message,
    create_qt_email_message,
    get_rap_fields,
    sort_rap_numbers,
    xstr,
    is_float,
    download_files,
    download_file
)


class TestUtils(TestCase):
    """Tests for utility functions in constants/utils.py."""

    def setUp(self):
        """Set up test data."""
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )

        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.write(b'Test file content')
        self.temp_file.close()

    def tearDown(self):
        """Clean up after tests."""
        # Remove temporary file
        if hasattr(self, 'temp_file'):
            os.unlink(self.temp_file.name)

    def test_get_attachment_storage_path(self):
        """Test the get_attachment_storage_path function."""
        filename = 'test_file.txt'
        expected_path = f'uploads/{self.user.username}/attachments/{filename}'

        # Create a mock instance with uploaded_by attribute
        class MockInstance:
            def __init__(self, user):
                self.uploaded_by = user

        mock_instance = MockInstance(self.user)

        result = get_attachment_storage_path(mock_instance, filename)
        self.assertEqual(result, expected_path)

    def test_split_email_list(self):
        """Test the split_email_list function."""
        # Test with different delimiters
        test_cases = [
            ('email1@example.com;email2@example.com', ['email1@example.com', 'email2@example.com']),
            ('email1@example.com,email2@example.com', ['email1@example.com', 'email2@example.com']),
            ('email1@example.com\temail2@example.com', ['email1@example.com', 'email2@example.com']),
            ('email1@example.com|email2@example.com', ['email1@example.com', 'email2@example.com']),
            ('email1@example.com email2@example.com', ['email1@example.com', 'email2@example.com']),
        ]

        for input_str, expected in test_cases:
            result = split_email_list(input_str)
            self.assertEqual(result, expected)

    def test_is_epa_email(self):
        """Test the is_epa_email function."""
        # Valid EPA emails
        self.assertTrue(is_epa_email('user@epa.gov'))
        self.assertTrue(is_epa_email('user.name@epa.gov'))
        self.assertTrue(is_epa_email('user-name@epa.gov'))
        self.assertTrue(is_epa_email('user_name@epa.gov'))

        # Invalid EPA emails
        self.assertFalse(is_epa_email('user@example.com'))
        self.assertFalse(is_epa_email('user@epa.gov.com'))
        self.assertFalse(is_epa_email('user@epa.gov.'))

    def test_non_epa_email_message(self):
        """Test the non_epa_email_message function."""
        emails = ['user1@example.com', 'user2@example.com']
        expected = "Email list may only contain @epa.gov addresses. " + \
            "Please sendnon-EPA emails directly from Outlook. " + \
            "Offending email(s): user1@example.com, user2@example.com"

        result = non_epa_email_message(emails)
        self.assertEqual(result, expected)

    def test_create_qt_email_message(self):
        """Test the create_qt_email_message function."""
        # Mock settings
        settings.EMAIL_DISCLAIMER = '<p>Disclaimer</p>'
        settings.EMAIL_DISCLAIMER_PLAIN = 'Disclaimer'
        settings.BCC_EMAIL = 'monitor@epa.gov'

        email_subject = 'Test Subject'
        text_content = 'Test Content\nWith newline'
        from_email = 'from@epa.gov'
        to_emails = ['to@epa.gov']
        carbon_copy = ['cc@epa.gov']
        blind_carbon_copy = ['bcc@epa.gov']

        email = create_qt_email_message(
            email_subject, text_content, from_email, to_emails,
            carbon_copy, blind_carbon_copy
        )

        # Check email properties
        self.assertEqual(email.subject, email_subject)
        self.assertEqual(email.from_email, from_email)
        self.assertEqual(email.to, to_emails)
        self.assertEqual(email.cc, carbon_copy)
        self.assertEqual(email.bcc, ['bcc@epa.gov', 'monitor@epa.gov'])

        # Check content
        self.assertIn('Disclaimer', email.body)
        self.assertIn('Test Content', email.body)
        self.assertIn('<br>', email.alternatives[0][0])

    def test_get_rap_fields_default(self):
        """Test the get_rap_fields function with default parameter."""
        expected = [
            'ace_rap_numbers', 'css_rap_numbers', 'sswr_rap_numbers',
            'hhra_rap_numbers', 'hsrp_rap_numbers',
            'hsrp_rap_extensions', 'shc_rap_numbers'
        ]

        result = get_rap_fields()
        self.assertEqual(result, expected)

    def test_get_rap_fields_form(self):
        """Test the get_rap_fields function with form parameter."""
        expected = [
            ['ace', 'ace_rap_numbers'], ['css', 'css_rap_numbers'],
            ['sswr', 'sswr_rap_numbers'], ['hhra', 'hhra_rap_numbers'],
            ['hsrp', 'hsrp_rap_numbers'], ['hsre', 'hsrp_rap_extensions'],
            ['shc', 'shc_rap_numbers']
        ]

        result = get_rap_fields('form')
        self.assertEqual(result, expected)

    def test_sort_rap_numbers(self):
        """Test the sort_rap_numbers function."""
        test_cases = [
            (['16.2.2', '16.1.1', '16.3.3'], ['16.1.1', '16.2.2', '16.3.3']),
            (['CIVA-2.5', '16.1.1', '16.3.3'], ['16.1.1', '16.3.3', 'CIVA-2.5']),
            (['16.2.2', 'CIVA-2.5', '16.1.1'], ['16.1.1', '16.2.2', 'CIVA-2.5']),
        ]

        for input_list, expected in test_cases:
            result = sort_rap_numbers(input_list)
            self.assertEqual(result, expected)

    def test_xstr(self):
        """Test the xstr function."""
        self.assertEqual(xstr(None), '')
        self.assertEqual(xstr('test'), 'test')
        self.assertEqual(xstr(123), '123')

    def test_is_float(self):
        """Test the is_float function."""
        self.assertTrue(is_float('123.45'))
        self.assertTrue(is_float('0'))
        self.assertTrue(is_float('-123.45'))
        self.assertFalse(is_float('abc'))
        self.assertFalse(is_float('12.34.56'))

    def test_download_files(self):
        """Test the download_files function."""
        # Create a mock file list
        class MockFile:
            def __init__(self, name):
                self.name = name
                self.file = type('obj', (object,), {'name': name})

        file_list = [
            MockFile(self.temp_file.name),
            MockFile(self.temp_file.name)
        ]
        zip_name = 'test_zip'

        response = download_files(file_list, zip_name)

        # Check response properties
        self.assertEqual(response['Content-Type'], 'application/force-download')
        self.assertEqual(response['Content-Disposition'], f'attachment; filename="{zip_name}.zip"')

        # Check zip content
        zip_data = BytesIO(response.content)
        with ZipFile(zip_data) as zip_file:
            self.assertEqual(len(zip_file.namelist()), 2)

    def test_download_file(self):
        """Test the download_file function."""
        # Create a mock file
        class MockFile:
            def __init__(self, name, file_path):
                self.name = name
                self.file = type('obj', (object,), {'name': file_path})

        # Test with regular file
        mock_file = MockFile('test.txt', self.temp_file.name)
        response = download_file(mock_file)

        self.assertEqual(response['Content-Disposition'], 'attachment; filename="test.txt"')

        # Test with Excel file
        excel_file = tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False)
        excel_file.close()

        mock_excel = MockFile('test.xlsx', excel_file.name)
        response = download_file(mock_excel)

        self.assertEqual(
            response['Content-Type'],
            'application/vnd.vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

        # Clean up
        os.unlink(excel_file.name)