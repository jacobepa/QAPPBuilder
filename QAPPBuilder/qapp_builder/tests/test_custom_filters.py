# test_custom_filters.py
# !/usr/bin/env python3
# coding=utf-8

from django.test import TestCase
from django import forms
from django.utils.safestring import SafeString
from django.contrib.auth.models import User

from qapp_builder.templatetags.custom_filters import as_epa, render_detail
from qapp_builder.models import Qapp, SectionA1


class TestForm(forms.Form):
    """Test form for testing custom filters."""
    test_field = forms.CharField(
        label='Test Field',
        required=True
    )


class TestCustomFilters(TestCase):
    """Tests for custom template filters."""

    def setUp(self):
        """Set up test data."""
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )

        # Create a test QAPP
        self.qapp = Qapp.objects.create(
            title='Test QAPP',
            created_by=self.user
        )

        # Create a test form field
        self.form = TestForm()
        self.field = self.form['test_field']

        # Create a test model instance
        self.section_a1 = SectionA1.objects.create(
            qapp=self.qapp,
            ord_center='Test Center',
            division='Test Division',
            branch='Test Branch',
            ord_national_program='Test Program',
            version_date='2024-01-01',
            proj_qapp_id='TEST-001',
            qa_category='A',
            intra_or_extra='INTRAMURALLY',
            accessibility=True
        )

    def test_as_epa_no_errors(self):
        """Test as_epa filter with no errors."""
        result = as_epa(self.field)

        # Check result is a SafeString
        self.assertIsInstance(result, SafeString)

        # Check HTML structure
        self.assertIn('<div class="usa-form-group">', result)
        self.assertIn('<label for="', result)
        self.assertIn('class="usa-label">', result)
        self.assertIn('Test Field', result)
        self.assertNotIn('usa-alert--error', result)

    def test_as_epa_with_errors(self):
        """Test as_epa filter with errors."""
        # Create a form with errors
        form_data = {'test_field': ''}
        form = TestForm(data=form_data)
        form.is_valid()  # This will trigger validation and set errors

        # Get the field with errors
        field_with_errors = form['test_field']

        result = as_epa(field_with_errors)

        # Check result is a SafeString
        self.assertIsInstance(result, SafeString)

        # Check HTML structure
        self.assertIn('<div class="usa-form-group">', result)
        self.assertIn('<label for="', result)
        self.assertIn('class="usa-label">', result)
        self.assertIn('Test Field', result)
        self.assertIn('usa-alert--error', result)
        self.assertIn('This field is required', result)

    def test_render_detail(self):
        """Test render_detail filter."""
        # Test with a string field
        result = render_detail(self.section_a1, 'ord_center')
        self.assertIsInstance(result, SafeString)
        self.assertIn('Test Center', result)

        # Test with a boolean field
        result = render_detail(self.section_a1, 'accessibility')
        self.assertIsInstance(result, SafeString)
        self.assertIn('True', result)

        # Test with a date field
        result = render_detail(self.section_a1, 'version_date')
        self.assertIsInstance(result, SafeString)
        self.assertIn('2024-01-01', result)
