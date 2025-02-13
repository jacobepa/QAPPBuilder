from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from qapp_builder.models import SectionA1, SectionA2, VersionControl, Definition
from .utility_forms import EpaBaseForm


class SectionA1Form(EpaBaseForm):
  """Form for Section A1. Contains special inputs Versions and Definitions."""

  class Meta:
    model = SectionA1
    exclude = ['section_a', 'qapp']
    widgets = {
      'version_date': forms.DateInput(
        format='%m/%d/%Y', attrs={'type': 'date', 'class': 'usa-input'}),
      'versions': FilteredSelectMultiple("Versions", is_stacked=True),
      'definitions': FilteredSelectMultiple("Definitions", is_stacked=False),
    }

  def __init__(self, *args, **kwargs):
    super(SectionA1Form, self).__init__(*args, **kwargs)
    # TODO: The versions won't be a selectable queryset.
    self.fields['versions'].queryset = VersionControl.objects.all()
    self.fields['definitions'].queryset = Definition.objects.all()


class SectionA2Form(EpaBaseForm):
  """Form for Section A2."""

  class Meta:
    model = SectionA2
    exclude = ['section_a', 'qapp']
