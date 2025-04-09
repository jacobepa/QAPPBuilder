# test_progress_views.py
# !/usr/bin/env python3
# coding=utf-8

from django.test import TestCase

from qapp_builder.models import (
    SectionA1, SectionA2, SectionA4, SectionA5, SectionA6,
    SectionA10, SectionA11, SectionB, SectionB7, SectionC, SectionD
)
from qapp_builder.views.progress_views import get_progress, get_qapp_page_list
from qapp_builder.tests.mixins import QappTestMixin


class TestProgressViews(QappTestMixin, TestCase):
    """Tests for progress views in qapp_builder/views/progress_views.py."""

    def setUp(self):
        """Set up test data."""
        # Create test user and QAPP
        self.user = self.create_test_user()
        self.qapp = self.create_test_qapp(self.user)

        # Create all test sections
        sections = self.create_all_test_sections(self.qapp)
        self.section_a1 = sections['section_a1']
        self.section_a2 = sections['section_a2']
        self.section_a4 = sections['section_a4']
        self.section_a5 = sections['section_a5']
        self.section_a6 = sections['section_a6']
        self.section_a10 = sections['section_a10']
        self.section_a11 = sections['section_a11']
        self.section_b = sections['section_b']
        self.section_b7 = sections['section_b7']
        self.section_c = sections['section_c']
        self.section_d = sections['section_d']

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
        # NOTE: SectionA10 is not required for QAPP completion
        # progress = get_progress(self.qapp.id, SectionA10)
        # self.assertGreater(progress, 0)

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
        new_qapp = self.create_test_qapp(self.user)

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
        # Get page list
        page_list = get_qapp_page_list(self.qapp.id)

        # Check page list
        self.assertIsInstance(page_list, list)
        self.assertGreater(len(page_list), 0)

        # Check page list structure
        for page in page_list:
            self.assertIn('label', page)
            self.assertIn('tail_path', page)
            self.assertIn('progress', page)
