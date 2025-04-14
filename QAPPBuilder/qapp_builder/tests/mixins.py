# mixins.py
# !/usr/bin/env python3
# coding=utf-8

from django.contrib.auth.models import User
from teams.models import Team, TeamMembership

from qapp_builder.models import (
    Qapp, SectionA1, SectionA2, SectionA4, SectionA5, SectionA6,
    SectionA10, SectionA11, SectionB, SectionB7, SectionC, SectionD,
    QappSharingTeamMap
)


class QappTestMixin:
    """Mixin for QAPP-related tests with common setup methods."""

    def create_test_user(self, username='testuser', password='12345',
                         is_superuser=False):
        """Create a test user."""
        if is_superuser:
            return User.objects.create_superuser(
                username=username,
                password=password,
                email=f'{username}@example.com'
            )
        return User.objects.create_user(
            username=username,
            password=password
        )

    def create_test_team(self, user=None, name='testteam'):
        """Create a test team."""
        if user is None:
            user = self.create_test_user()
        return Team.objects.create(
            created_by=user,
            name=name,
            last_modified_by=user
        )

    def create_test_team_membership(self, user=None, team=None,
                                   is_owner=True, can_edit=True):
        """Create a test team membership."""
        if user is None:
            user = self.create_test_user()
        if team is None:
            team = self.create_test_team(user)
        return TeamMembership.objects.create(
            member=user,
            team=team,
            is_owner=is_owner,
            can_edit=can_edit
        )

    def create_test_qapp(self, user=None, title='Test QAPP'):
        """Create a test QAPP."""
        if user is None:
            user = self.create_test_user()
        return Qapp.objects.create(
            title=title,
            created_by=user
        )

    def create_test_qapp_sharing(self, qapp=None, team=None, can_edit=True):
        """Create a test QAPP sharing."""
        if qapp is None:
            qapp = self.create_test_qapp()
        if team is None:
            team = self.create_test_team()
        return QappSharingTeamMap.objects.create(
            qapp=qapp,
            team=team,
            can_edit=can_edit
        )

    def create_test_section_a1(self, qapp=None, user=None):
        """Create a test SectionA1."""
        if qapp is None:
            qapp = self.create_test_qapp(user)
        return SectionA1.objects.create(
            qapp=qapp,
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

    def create_test_section_a2(self, qapp=None, user=None):
        """Create a test SectionA2."""
        if qapp is None:
            qapp = self.create_test_qapp(user)
        return SectionA2.objects.create(
            qapp=qapp,
            ord_technical_lead='Test Lead',
            ord_tl_supervisor='Test Supervisor',
            ord_qa_manager='Test QA Manager'
        )

    def create_test_section_a4(self, qapp=None, user=None):
        """Create a test SectionA4."""
        if qapp is None:
            qapp = self.create_test_qapp(user)
        return SectionA4.objects.create(
            qapp=qapp,
            project_background='Test Background',
            project_purpose='Test Purpose'
        )

    def create_test_section_a5(self, qapp=None, user=None):
        """Create a test SectionA5."""
        if qapp is None:
            qapp = self.create_test_qapp(user)
        return SectionA5.objects.create(
            qapp=qapp,
            tasks_summary='Test Summary',
            start_fy=25,
            start_q=1
        )

    def create_test_section_a6(self, qapp=None, user=None):
        """Create a test SectionA6."""
        if qapp is None:
            qapp = self.create_test_qapp(user)
        return SectionA6.objects.create(
            qapp=qapp,
            information='Test Information'
        )

    def create_test_section_a10(self, qapp=None, user=None):
        """Create a test SectionA10."""
        if qapp is None:
            qapp = self.create_test_qapp(user)
        return SectionA10.objects.create(
            qapp=qapp
        )

    def create_test_section_a11(self, qapp=None, user=None):
        """Create a test SectionA11."""
        if qapp is None:
            qapp = self.create_test_qapp(user)
        return SectionA11.objects.create(
            qapp=qapp,
            information='Test Information'
        )

    def create_test_section_b(self, qapp=None, user=None):
        """Create a test SectionB."""
        if qapp is None:
            qapp = self.create_test_qapp(user)
        return SectionB.objects.create(
            qapp=qapp,
            b1='Test B1',
            b2='Test B2',
            b3='Test B3',
            b4='Test B4',
            b5='Test B5',
            b6='Test B6'
        )

    def create_test_section_b7(self, qapp=None, user=None):
        """Create a test SectionB7."""
        if qapp is None:
            qapp = self.create_test_qapp(user)
        return SectionB7.objects.create(
            qapp=qapp,
            b71='Test B71',
            b72='Test B72'
        )

    def create_test_section_c(self, qapp=None, user=None):
        """Create a test SectionC."""
        if qapp is None:
            qapp = self.create_test_qapp(user)
        return SectionC.objects.create(
            qapp=qapp,
            c2='Test C2'
        )

    def create_test_section_d(self, qapp=None, user=None):
        """Create a test SectionD."""
        if qapp is None:
            qapp = self.create_test_qapp(user)
        return SectionD.objects.create(
            qapp=qapp,
            d1='Test D1',
            d2='Test D2'
        )

    def create_all_test_sections(self, qapp=None, user=None):
        """Create all test sections for a QAPP."""
        if qapp is None:
            qapp = self.create_test_qapp(user)
        return {
            'section_a1': self.create_test_section_a1(qapp),
            'section_a2': self.create_test_section_a2(qapp),
            'section_a4': self.create_test_section_a4(qapp),
            'section_a5': self.create_test_section_a5(qapp),
            'section_a6': self.create_test_section_a6(qapp),
            'section_a10': self.create_test_section_a10(qapp),
            'section_a11': self.create_test_section_a11(qapp),
            'section_b': self.create_test_section_b(qapp),
            'section_b7': self.create_test_section_b7(qapp),
            'section_c': self.create_test_section_c(qapp),
            'section_d': self.create_test_section_d(qapp),
        }