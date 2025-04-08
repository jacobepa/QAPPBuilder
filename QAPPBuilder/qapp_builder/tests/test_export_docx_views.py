# test_export_docx_views.py
# !/usr/bin/env python3
# coding=utf-8

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from qapp_builder.models import Qapp, SectionA1
from teams.models import Team, TeamMembership
from docx import Document
from io import BytesIO
import constants.qapp_section_a_const as constants_a


class TestExportDocxViews(TestCase):
    """Tests for the export_docx_views module."""

    def setUp(self):
        """Set up test data."""
        # Create test users
        self.user1 = User.objects.create_user(
            username='testuser1',
            password='12345'
        )
        self.user2 = User.objects.create_user(
            username='testuser2',
            password='12345'
        )

        # Create test team
        self.team = Team.objects.create(
            created_by=self.user1,
            name='testteam',
            last_modified_by=self.user1
        )

        # Create team membership
        TeamMembership.objects.create(
            member=self.user1,
            team=self.team,
            is_owner=True,
            can_edit=True
        )

        # Create test QAPP
        self.qapp = Qapp.objects.create(
            title='Test QAPP',
            created_by=self.user1
        )

        # Create SectionA1 for the QAPP
        self.section_a1 = SectionA1.objects.create(
            qapp=self.qapp,
            ord_center='Test Center',
            division='Test Division',
            branch='Test Branch',
            ord_national_program='Test Program',
            version_date='2024-01-01',
            proj_qapp_id='TEST-001',
            qa_category='A',
            intra_or_extra=constants_a.INTRAMURALLY,
            accessibility=True
        )

        # Set up client
        self.client = Client()
        self.client.login(username='testuser1', password='12345')

    def test_export_qapp_docx_authenticated(self):
        """Test exporting QAPP as DOCX when authenticated."""
        response = self.client.get(
            reverse('export_qapp_docx', args=[self.qapp.id])
        )

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check content type
        self.assertEqual(
            response['Content-Type'],
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )

        # Check filename
        expected_filename = f'{self.qapp.title} - {constants_a.QAPP_STR}.docx'
        self.assertEqual(
            response['Content-Disposition'],
            f'attachment; filename="{expected_filename}"'
        )

        # Verify document content
        doc = Document(BytesIO(response.content))

        # Check document has content
        self.assertTrue(len(doc.paragraphs) > 0)

        # Check for section headers
        section_headers = [p.text for p in doc.paragraphs if p.style.name.startswith('Heading')]
        self.assertTrue(any('Section A' in header for header in section_headers))

    def test_export_qapp_docx_unauthenticated(self):
        """Test exporting QAPP as DOCX when not authenticated."""
        # Logout the client
        self.client.logout()

        response = self.client.get(
            reverse('export_qapp_docx', args=[self.qapp.id])
        )

        # Should redirect to login page
        self.assertEqual(response.status_code, 302)
        self.assertTrue('/accounts/login/' in response.url)

    def test_export_qapp_docx_nonexistent(self):
        """Test exporting non-existent QAPP."""
        response = self.client.get(
            reverse('export_qapp_docx', args=[999])
        )

        # Should return 404
        self.assertEqual(response.status_code, 404)

    def test_export_qapp_docx_content(self):
        """Test the content of the exported DOCX file."""
        response = self.client.get(
            reverse('export_qapp_docx', args=[self.qapp.id])
        )

        doc = Document(BytesIO(response.content))

        # Check for QAPP title
        title_found = False
        for paragraph in doc.paragraphs:
            if self.qapp.title in paragraph.text:
                title_found = True
                break
        self.assertTrue(title_found)

        # Check for Section A1 content
        section_a1_content = [
            self.section_a1.ord_center,
            self.section_a1.division,
            self.section_a1.branch,
            self.section_a1.ord_national_program,
            self.section_a1.proj_qapp_id,
            self.section_a1.qa_category
        ]

        content_found = {content: False for content in section_a1_content}
        for paragraph in doc.paragraphs:
            for content in section_a1_content:
                if content in paragraph.text:
                    content_found[content] = True

        # All Section A1 content should be found
        self.assertTrue(all(content_found.values()))