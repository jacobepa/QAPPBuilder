from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from qapp_builder.models import SectionA1, SectionA2, VersionControl, Definition
from .utility_forms import EpaBaseForm


class SectionA1Form(EpaBaseForm):

  class Meta:
    model = SectionA1
    exclude = ['section_a', 'qapp']
    widgets = {
      'version_date': forms.DateInput(
        format='%m/%d/%Y', attrs={'type': 'date', 'class': 'usa-input'}),
      'mou_date': forms.DateInput(
        format='%m/%d/%Y', attrs={'type': 'date', 'class': 'usa-input'}),
      'enf_legal_date': forms.DateInput(
        format='%m/%d/%Y', attrs={'type': 'date', 'class': 'usa-input'}),
      'definitions': FilteredSelectMultiple("Definitions", is_stacked=False),
    }

  def __init__(self, *args, **kwargs):
    super(SectionA1Form, self).__init__(*args, **kwargs)
    self.fields['definitions'].queryset = Definition.objects.all()


class VersionControlForm(EpaBaseForm):

  class Meta:
    model = VersionControl
    exclude = ['qapp_id', 'updated_on', 'section_a']


VersionControlFormSet = forms.inlineformset_factory(
  SectionA1, VersionControl, form=VersionControlForm, extra=1, can_delete=False
)


class SectionA2Form(EpaBaseForm):
  """Form for Section A2."""

  class Meta:
    model = SectionA2
    exclude = ['section_a', 'qapp']
