# test_inheritable_views.py
# !/usr/bin/env python3
# coding=utf-8

from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView

from qapp_builder.models import Qapp, SectionA1, QappSharingTeamMap
from teams.models import Team, TeamMembership
from qapp_builder.views.inheritable_views import (
    check_can_edit,
    QappBuilderPrivateView,
    SectionTemplateView,
    SectionCreateBase,
    SectionUpdateBase,
    SectionDetailBase
)


class TestInheritableViews(TestCase):
    """Tests for inheritable views."""

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
        self.superuser = User.objects.create_superuser(
            username='admin',
            password='admin123',
            email='admin@example.com'
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
            intra_or_extra='INTRAMURALLY',
            accessibility=True
        )

        # Set up client
        self.client = Client()
        self.factory = RequestFactory()

    def test_check_can_edit_unauthenticated(self):
        """Test check_can_edit with unauthenticated user."""
        can_edit, response = check_can_edit(self.qapp, self.user2)

        self.assertFalse(can_edit)
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertEqual(response.url, reverse('login'))

    def test_check_can_edit_superuser(self):
        """Test check_can_edit with superuser."""
        can_edit, response = check_can_edit(self.qapp, self.superuser)

        self.assertTrue(can_edit)
        self.assertIsNone(response)

    def test_check_can_edit_owner(self):
        """Test check_can_edit with QAPP owner."""
        can_edit, response = check_can_edit(self.qapp, self.user1)

        self.assertTrue(can_edit)
        self.assertIsNone(response)

    def test_check_can_edit_team_member(self):
        """Test check_can_edit with team member."""
        # Create team sharing with edit permission
        QappSharingTeamMap.objects.create(
            qapp=self.qapp,
            team=self.team,
            can_edit=True
        )

        can_edit, response = check_can_edit(self.qapp, self.user1)

        self.assertTrue(can_edit)
        self.assertIsNone(response)

    def test_check_can_edit_nonexistent_qapp(self):
        """Test check_can_edit with nonexistent QAPP."""
        can_edit, response = check_can_edit(999, self.user1)

        self.assertFalse(can_edit)
        self.assertIsNone(response)

    def test_qapp_builder_private_view(self):
        """Test QappBuilderPrivateView."""
        # Create a test view class
        class TestView(QappBuilderPrivateView, TemplateView):
            template_name = 'qapp/generic_form.html'

        # Create request
        request = self.factory.get('/')
        request.user = self.user1

        # Create view instance
        view = TestView()
        view.request = request
        view.kwargs = {'qapp_id': self.qapp.id}

        # Get context data
        context = view.get_context_data()

        # Check context
        self.assertIn('user_can_edit', context)
        self.assertTrue(context['user_can_edit'][0])

    def test_section_template_view(self):
        """Test SectionTemplateView."""
        # Create a test view class
        class TestView(SectionTemplateView):
            template_name = 'qapp/generic_form.html'
            section_title = 'Test Section'
            previous_url_name = 'sectiona1_detail'
            next_url_name = 'sectiona2_detail'
            current_page = 1

        # Create request
        request = self.factory.get('/')
        request.user = self.user1

        # Create view instance
        view = TestView()
        view.request = request
        view.kwargs = {'qapp_id': self.qapp.id}

        # Get context data
        context = view.get_context_data()

        # Check context
        self.assertEqual(context['title'], 'Test Section')
        self.assertEqual(context['qapp_id'], self.qapp.id)
        self.assertEqual(context['current_page'], 1)
        self.assertIn('page_list', context)

    def test_section_create_base(self):
        """Test SectionCreateBase."""
        # Create a test view class
        class TestView(SectionCreateBase):
            model = SectionA1
            fields = ['ord_center', 'division', 'branch']
            section_title = 'Test Section'
            previous_url_name = 'sectiona1_detail'
            next_url_name = 'sectiona2_detail'
            detail_url_name = 'sectiona1_detail'
            current_page = 1

        # Create request
        request = self.factory.get('/')
        request.user = self.user1

        # Create view instance
        view = TestView()
        view.request = request
        view.kwargs = {'qapp_id': self.qapp.id}

        # Test dispatch with existing object
        response = view.dispatch(request)
        self.assertIsInstance(response, HttpResponseRedirect)

        # Test dispatch with nonexistent object
        view.kwargs = {'qapp_id': 999}
        response = view.dispatch(request)
        self.assertIsInstance(response, HttpResponse)

    def test_section_update_base(self):
        """Test SectionUpdateBase."""
        # Create a test view class
        class TestView(SectionUpdateBase):
            model = SectionA1
            fields = ['ord_center', 'division', 'branch']
            section_title = 'Test Section'
            previous_url_name = 'sectiona1_detail'
            detail_url_name = 'sectiona1_detail'
            current_page = 1

        # Create request
        request = self.factory.get('/')
        request.user = self.user1

        # Create view instance
        view = TestView()
        view.request = request
        view.kwargs = {'qapp_id': self.qapp.id}

        # Test dispatch
        response = view.dispatch(request)
        self.assertIsInstance(response, HttpResponse)

    def test_section_detail_base(self):
        """Test SectionDetailBase."""
        # Create a test view class
        class TestView(SectionDetailBase):
            model = SectionA1
            section_title = 'Test Section'
            previous_url_name = 'sectiona1_detail'
            next_url_name = 'sectiona2_detail'
            edit_url_name = 'sectiona1_edit'
            create_url_name = 'sectiona1_create'
            current_page = 1

        # Create request
        request = self.factory.get('/')
        request.user = self.user1

        # Create view instance
        view = TestView()
        view.request = request
        view.kwargs = {'qapp_id': self.qapp.id}

        # Test dispatch with existing object
        response = view.dispatch(request)
        self.assertIsInstance(response, HttpResponse)

        # Test dispatch with nonexistent object
        view.kwargs = {'qapp_id': 999}
        response = view.dispatch(request)
        self.assertIsInstance(response, HttpResponseRedirect)