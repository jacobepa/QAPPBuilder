# test_views.py (qapp_builder)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# py-lint: disable=W0511,R0904
"""
This file demonstrates writing tests using the unittest module.

These will pass when you run "manage.py test".
"""

from datetime import datetime
import django
from django.db.models.query import QuerySet, EmptyQuerySet
from django.test import Client, TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from qapp_builder.models import Qapp, QappSharingTeamMap, SectionA1
from qapp_builder.forms.qapp_forms import QappForm
from qapp_builder.views.qapp_views import (
    check_can_edit, get_qapp_all, QappEdit
)
from teams.models import Team, TeamMembership


class TestViewAuthenticated(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS.
        @classmethod
        def setUpClass(cls):
            """Prepare objects for testing."""
            super(TestViewAuthenticated, cls).setUpClass()
            django.setup()

    def setUp(self):
        """Prepare various objects for this class of tests."""
        self.request_factory = RequestFactory()
        self.test_str = 'Test'
        self.client = Client()
        # User 1 created the team, User 2 created ExistingData,
        # User 3 has no privileges
        self.user1 = User.objects.create_user(
            username='testuser1',
            password='12345'
        )
        self.user2 = User.objects.create_user(
            username='testuser2',
            password='12345'
        )
        self.client.login(username='testuser1', password='12345')
        self.user = User.objects.get(id=1)
        self.team = Team.objects.create(
            created_by=self.user1,
            name='testteam',
            last_modified_by=self.user1
        )
        self.team2 = Team.objects.create(
            created_by=self.user,
            name='testteam2',
            last_modified_by=self.user
        )
        TeamMembership.objects.create(
            member=self.user1,
            team=self.team,
            is_owner=True,
            can_edit=True
        )
        TeamMembership.objects.create(
            member=self.user,
            team=self.team,
            is_owner=True,
            can_edit=True
        )
        TeamMembership.objects.create(
            member=self.user,
            team=self.team2,
            is_owner=True,
            can_edit=True
        )
        # Build some models to be used in this test class:
        self.form = QappForm()

        # Create Qapp with required fields
        self.qapp = Qapp.objects.create(
            title='Test QAPP',
            created_by=self.user
        )

        # Create SectionA1 with the additional fields
        self.section_a1 = SectionA1.objects.create(
            qapp=self.qapp,
            ord_center='Center for Environmental Solutions & Emergency Response',
            division='Test Division',
            branch='Test Branch',
            ord_national_program='Test Program',
            version_date=datetime.now().date(),
            proj_qapp_id='Test ID',
            qa_category='A',
            intra_or_extra='Intramurally'
        )

        self.dat_team_map = QappSharingTeamMap.objects.create(
            qapp=self.qapp,
            team=self.team,
            can_edit=True
        )

    def test_get_qapp_all(self):
        """
        Test the get all qapp method.

        This should return the one qapp that was created during setup.
        """
        data = get_qapp_all()
        self.assertIsInstance(data, QuerySet)
        self.assertNotIsInstance(data, EmptyQuerySet)
        self.assertEqual(len(data), 1)

    def test_qapp_index(self):
        """Test the qapp module index page."""
        response = self.client.get('/')
        self.assertContains(
            response, 'Quality Assurance (QA) Project Plan Development', 1, 200)
        self.assertContains(response, 'New QAPP', 1, 200)
        self.assertContains(response, 'New Team', 1, 200)
        self.assertContains(response, 'View QAPPs by User', 1, 200)
        self.assertContains(response, 'View QAPPs by Team', 1, 200)

    def test_qapp_list_user(self):
        """Test the qapp list page for a User."""
        response = self.client.get('/qapp/list/user/1/')
        self.assertContains(response, 'QUALITY ASSURANCE PROJECT PLAN', 1, 200)
        self.assertContains(response, 'Create a new QAPP', 1, 200)
        self.assertContains(response, 'View or Edit Existing QAPP', 1, 200)
        self.assertContains(response, 'Export All QAPP', 2, 200)
        self.assertContains(response, 'Export All QAPP to Word Doc', 1, 200)
        self.assertContains(response, 'Export All QAPP to PDF', 1, 200)

    def test_qapp_list_team(self):
        """Test the qapp list page for a Team."""
        response = self.client.get('/qapp/list/team/1/')
        self.assertContains(response, 'QUALITY ASSURANCE PROJECT PLAN', 1, 200)
        self.assertContains(response, 'Create a new QAPP', 1, 200)
        self.assertContains(response, 'View or Edit Existing QAPP', 1, 200)
        self.assertContains(response, 'Export All QAPP', 2, 200)
        self.assertContains(response, 'Export All QAPP to Word Doc', 1, 200)
        self.assertContains(response, 'Export All QAPP to PDF', 1, 200)

    def test_check_can_edit_user_true(self):
        """Test the check_can_edit method when the user CAN edit."""
        can_edit = check_can_edit(self.qapp, self.user)
        self.assertTrue(can_edit)

    def test_check_can_edit_team_true(self):
        """Test the check_can_edit method when the user team CAN edit."""
        can_edit = check_can_edit(self.qapp, self.user1)
        self.assertTrue(can_edit)

    def test_check_can_edit_false(self):
        """Test the check_can_edit method when the user CANNOT edit."""
        can_edit = check_can_edit(self.qapp, self.user2)
        self.assertFalse(can_edit)

    def test_qapp_update_get_allowed(self):
        """Test the QappEdit view GET method with default (permitted) user."""
        response = self.client.get(f'/qapp/{self.qapp.id}/edit/')
        self.assertContains(response, 'Title', 1, 200)
        self.assertContains(response, 'Share With Teams', 1, 200)
        self.assertContains(response, 'Save', 1, 200)
        self.assertContains(response, 'Reset', 1, 200)
        self.assertContains(response, 'Cancel', 1, 200)

    def test_qapp_update_get_denied(self):
        """Test the QappEdit view GET method with non-permitted user."""
        request = self.request_factory.get(f'/qapp/{self.qapp.id}/edit/')
        request.user = self.user2
        response = QappEdit.as_view()(request, pk=str(self.qapp.id))
        self.assertEqual(response.status_code, 403)

    def test_qapp_update_form_valid(self):
        """Test the QappEdit form_valid method."""
        data = {
            'title': 'Updated QAPP Title',
            'teams': [self.team2.id]
        }
        response = self.client.post(f'/qapp/{self.qapp.id}/edit/', data=data)
        self.assertEqual(response.status_code, 302)
        # Verify the update
        updated_qapp = Qapp.objects.get(id=self.qapp.id)
        self.assertEqual(updated_qapp.title, 'Updated QAPP Title')
        self.assertTrue(updated_qapp.teams.filter(id=self.team2.id).exists())

    def test_qapp_create_get(self):
        """Test the QappCreate view GET method."""
        response = self.client.get('/qapp/create/')
        self.assertContains(response, 'Title', 1, 200)
        self.assertContains(response, 'Share With Teams', 1, 200)
        self.assertContains(response, 'Save', 1, 200)
        self.assertContains(response, 'Reset', 1, 200)
        self.assertContains(response, 'Cancel', 1, 200)

    def test_qapp_create_post(self):
        """Test the QappCreate view POST method."""
        data = {
            'title': 'New QAPP',
            'teams': [self.team.id]
        }
        response = self.client.post('/qapp/create/', data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Qapp.objects.count(), 2)

    def test_qapp_create_post_2(self):
        """
        Test Create Qapp with a non-valid form.

        This should render the create page again.
        """
        response = self.client.post('/qapp/create/', data={})
        self.assertContains(response, 'Title', 1, 200)
        self.assertContains(response, 'Share With Teams', 1, 200)
        self.assertContains(response, 'Save', 1, 200)
        self.assertContains(response, 'Reset', 1, 200)
        self.assertContains(response, 'Cancel', 1, 200)

    def test_qapp_edit(self):
        response = self.client.get(f'/qapp/{self.qapp.pk}/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'qapp/qapp_form.html')

    def test_qapp_edit_form_valid(self):
        response = self.client.post(
            f'/qapp/{self.qapp.pk}/edit/',
            {
                'title': 'Updated QAPP',
            }
        )
        self.assertEqual(response.status_code, 302)
        self.qapp.refresh_from_db()
        self.assertEqual(self.qapp.title, 'Updated QAPP')

    def test_qapp_detail(self):
        response = self.client.get(
            f'/qapp/{self.qapp.pk}/detail/'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'qapp/qapp_detail.html'
        )

    def test_qapp_create(self):
        response = self.client.get('/qapp/create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'qapp/qapp_form.html')

    def test_qapp_create_form_valid(self):
        response = self.client.post(
            '/qapp/create/',
            {
                'title': 'New QAPP',
                'description': 'New description'
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Qapp.objects.filter(title='New QAPP').exists())
