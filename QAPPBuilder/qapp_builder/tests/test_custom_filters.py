# test_custom_filters.py
# !/usr/bin/env python3
# coding=utf-8

from django.test import TestCase
from django import forms
from django.utils.safestring import SafeString

from qapp_builder.templatetags.custom_filters import as_epa, render_detail
from qapp_builder.models import SectionA1


class TestCustomFilters(TestCase):
    """Tests for custom template filters in qapp_builder/templatetags/custom_filters.py."""

    def setUp(self):
        """Set up test data."""
        # Create a test form field
        class TestForm(forms.Form):
            test_field = forms.CharField(
                label='Test Field',
                required=True
            )

        self.form = TestForm()
        self.field = self.form['test_field']

        # Create a test model instance
        self.section_a1 = SectionA1.objects.create(
            qapp_id=1,
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
        # Add errors to the field
        self.field.errors = ['This field is required']

        result = as_epa(self.field)

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
