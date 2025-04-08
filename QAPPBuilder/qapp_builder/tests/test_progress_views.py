# test_progress_views.py
# !/usr/bin/env python3
# coding=utf-8

from django.test import TestCase
from django.contrib.auth.models import User

from qapp_builder.models import (
    Qapp, SectionA1, SectionA2, SectionA4, SectionA5, SectionA6,
    SectionA10, SectionA11, SectionB, SectionB7, SectionC, SectionD
)
from qapp_builder.views.progress_views import get_progress, get_qapp_page_list


class TestProgressViews(TestCase):
    """Tests for progress views in qapp_builder/views/progress_views.py."""

    def setUp(self):
        """Set up test data."""
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )

        # Create test QAPP
        self.qapp = Qapp.objects.create(
            title='Test QAPP',
            created_by=self.user
        )

        # Create test sections
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

        self.section_a2 = SectionA2.objects.create(
            qapp=self.qapp,
            project_title='Test Project',
            project_id='TEST-001',
            project_description='Test Description'
        )

        self.section_a4 = SectionA4.objects.create(
            qapp=self.qapp,
            qa_category='A',
            qa_category_other='Other Category'
        )

        self.section_a5 = SectionA5.objects.create(
            qapp=self.qapp,
            project_manager='Test Manager',
            project_manager_email='manager@epa.gov'
        )

        self.section_a6 = SectionA6.objects.create(
            qapp=self.qapp,
            organization='Test Org',
            division='Test Division',
            branch='Test Branch'
        )

        self.section_a10 = SectionA10.objects.create(
            qapp=self.qapp,
            data_quality_objectives='Test DQOs'
        )

        self.section_a11 = SectionA11.objects.create(
            qapp=self.qapp,
            project_specific_requirements='Test Requirements'
        )

        self.section_b = SectionB.objects.create(
            qapp=self.qapp,
            sampling_design='Test Design'
        )

        self.section_b7 = SectionB7.objects.create(
            qapp=self.qapp,
            data_review='Test Review'
        )

        self.section_c = SectionC.objects.create(
            qapp=self.qapp,
            data_generation='Test Generation'
        )

        self.section_d = SectionD.objects.create(
            qapp=self.qapp,
            data_reduction='Test Reduction'
        )

    def test_get_progress_with_existing_section(self):
        """Test get_progress with an existing section."""
        # Test with SectionA1
        progress = get_progress(self.qapp.id, SectionA1)
        self.assertGreater(progress, 0)

        # Test with SectionA2
        progress = get_progress(self.qapp.id, SectionA2)
        self.assertGreater(progress, 0)

        # Test with SectionA4
        progress = get_progress(self.qapp.id, SectionA4)
        self.assertGreater(progress, 0)

        # Test with SectionA5
        progress = get_progress(self.qapp.id, SectionA5)
        self.assertGreater(progress, 0)

        # Test with SectionA6
        progress = get_progress(self.qapp.id, SectionA6)
        self.assertGreater(progress, 0)

        # Test with SectionA10
        progress = get_progress(self.qapp.id, SectionA10)
        self.assertGreater(progress, 0)

        # Test with SectionA11
        progress = get_progress(self.qapp.id, SectionA11)
        self.assertGreater(progress, 0)

        # Test with SectionB
        progress = get_progress(self.qapp.id, SectionB)
        self.assertGreater(progress, 0)

        # Test with SectionB7
        progress = get_progress(self.qapp.id, SectionB7)
        self.assertGreater(progress, 0)

        # Test with SectionC
        progress = get_progress(self.qapp.id, SectionC)
        self.assertGreater(progress, 0)

        # Test with SectionD
        progress = get_progress(self.qapp.id, SectionD)
        self.assertGreater(progress, 0)

    def test_get_progress_with_nonexistent_section(self):
        """Test get_progress with a nonexistent section."""
        # Create a new QAPP without any sections
        new_qapp = Qapp.objects.create(
            title='New QAPP',
            created_by=self.user
        )

        # Test with SectionA1
        progress = get_progress(new_qapp.id, SectionA1)
        self.assertEqual(progress, 0)

        # Test with SectionA2
        progress = get_progress(new_qapp.id, SectionA2)
        self.assertEqual(progress, 0)

        # Test with SectionA4
        progress = get_progress(new_qapp.id, SectionA4)
        self.assertEqual(progress, 0)

        # Test with SectionA5
        progress = get_progress(new_qapp.id, SectionA5)
        self.assertEqual(progress, 0)

        # Test with SectionA6
        progress = get_progress(new_qapp.id, SectionA6)
        self.assertEqual(progress, 0)

        # Test with SectionA10
        progress = get_progress(new_qapp.id, SectionA10)
        self.assertEqual(progress, 0)

        # Test with SectionA11
        progress = get_progress(new_qapp.id, SectionA11)
        self.assertEqual(progress, 0)

        # Test with SectionB
        progress = get_progress(new_qapp.id, SectionB)
        self.assertEqual(progress, 0)

        # Test with SectionB7
        progress = get_progress(new_qapp.id, SectionB7)
        self.assertEqual(progress, 0)

        # Test with SectionC
        progress = get_progress(new_qapp.id, SectionC)
        self.assertEqual(progress, 0)

        # Test with SectionD
        progress = get_progress(new_qapp.id, SectionD)
        self.assertEqual(progress, 0)

    def test_get_qapp_page_list(self):
        """Test get_qapp_page_list function."""
        page_list = get_qapp_page_list(self.qapp.id)

        # Check page list structure
        self.assertIsInstance(page_list, list)
        self.assertEqual(len(page_list), 17)  # Total number of pages

        # Check first page (QAPP Details)
        self.assertEqual(page_list[0]['tail_path'], '/detail/')
        self.assertEqual(page_list[0]['label'], 'QAPP Details')
        self.assertGreater(page_list[0]['progress'], 0)

        # Check Section A1
        self.assertEqual(page_list[1]['tail_path'], '/section-a1/detail/')
        self.assertEqual(page_list[1]['label'], 'Section A1')
        self.assertGreater(page_list[1]['progress'], 0)

        # Check Section A2
        self.assertEqual(page_list[2]['tail_path'], '/section-a2/detail/')
        self.assertEqual(page_list[2]['label'], 'Section A2')
        self.assertGreater(page_list[2]['progress'], 0)

        # Check Section A3 (static progress)
        self.assertEqual(page_list[3]['tail_path'], '/section-a3/')
        self.assertEqual(page_list[3]['label'], 'Section A3')
        self.assertEqual(page_list[3]['progress'], 100)

        # Check Section A4
        self.assertEqual(page_list[4]['tail_path'], '/section-a4/detail/')
        self.assertEqual(page_list[4]['label'], 'Section A4')
        self.assertGreater(page_list[4]['progress'], 0)

        # Check Section A5
        self.assertEqual(page_list[5]['tail_path'], '/section-a5/detail/')
        self.assertEqual(page_list[5]['label'], 'Section A5')
        self.assertGreater(page_list[5]['progress'], 0)

        # Check Section A6
        self.assertEqual(page_list[6]['tail_path'], '/section-a6/detail/')
        self.assertEqual(page_list[6]['label'], 'Section A6')
        self.assertGreater(page_list[6]['progress'], 0)

        # Check Section A7 (static progress)
        self.assertEqual(page_list[7]['tail_path'], '/section-a7/')
        self.assertEqual(page_list[7]['label'], 'Section A7')
        self.assertEqual(page_list[7]['progress'], 100)

        # Check Section A8 (static progress)
        self.assertEqual(page_list[8]['tail_path'], '/section-a8/')
        self.assertEqual(page_list[8]['label'], 'Section A8')
        self.assertEqual(page_list[8]['progress'], 100)

        # Check Section A9 (static progress)
        self.assertEqual(page_list[9]['tail_path'], '/section-a9/')
        self.assertEqual(page_list[9]['label'], 'Section A9')
        self.assertEqual(page_list[9]['progress'], 100)

        # Check Section A10
        self.assertEqual(page_list[10]['tail_path'], '/section-a10/detail/')
        self.assertEqual(page_list[10]['label'], 'Section A10')
        self.assertGreater(page_list[10]['progress'], 0)

        # Check Section A11
        self.assertEqual(page_list[11]['tail_path'], '/section-a11/detail/')
        self.assertEqual(page_list[11]['label'], 'Section A11')
        self.assertGreater(page_list[11]['progress'], 0)

        # Check Section A12 (static progress)
        self.assertEqual(page_list[12]['tail_path'], '/section-a12/')
        self.assertEqual(page_list[12]['label'], 'Section A12')
        self.assertEqual(page_list[12]['progress'], 100)

        # Check Section B
        self.assertEqual(page_list[13]['tail_path'], '/section-b/detail/')
        self.assertEqual(page_list[13]['label'], 'Section B')
        self.assertGreater(page_list[13]['progress'], 0)

        # Check Section B7
        self.assertEqual(page_list[14]['tail_path'], '/section-b7/detail/')
        self.assertEqual(page_list[14]['label'], 'Section B7')
        self.assertGreater(page_list[14]['progress'], 0)

        # Check Section C
        self.assertEqual(page_list[15]['tail_path'], '/section-c/detail/')
        self.assertEqual(page_list[15]['label'], 'Section C')
        self.assertGreater(page_list[15]['progress'], 0)

        # Check Section D
        self.assertEqual(page_list[16]['tail_path'], '/section-d/detail/')
        self.assertEqual(page_list[16]['label'], 'Section D')
        self.assertGreater(page_list[16]['progress'], 0)