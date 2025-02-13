from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from qapp_builder.models import SectionA1, SectionA2,   SectionA4, SectionA5, SectionA6, SectionA7, SectionA8, SectionA9, SectionA10, SectionA11, SectionA12, VersionControl, Definition
from .utility_forms import EpaBaseForm


class SectionA1Form(EpaBaseForm):
  """Form for Section A1. Contains special inputs Versions and Definitions."""

  class Meta:
    model = SectionA1
    exclude = ['section_a', 'qapp']
    widgets = {
      'version_date': forms.DateInput(
        format='%m/%d/%Y', attrs={'type': 'date', 'class': 'usa-input'}),
      'versions': FilteredSelectMultiple("Versions", is_stacked=False),
      'definitions': FilteredSelectMultiple("Definitions", is_stacked=False),
    }

  def __init__(self, *args, **kwargs):
    super(SectionA1Form, self).__init__(*args, **kwargs)
    self.fields['versions'].queryset = VersionControl.objects.all()
    self.fields['definitions'].queryset = Definition.objects.all()


class SectionA2Form(EpaBaseForm):
  """Form for Section A2."""

  class Meta:
    model = SectionA2
    exclude = ['section_a', 'qapp']
    labels = {
      'epa_op_man': 'Signature of EPA Operations Manager',
      'epa_qam': 'Signature of EPA QAM, or designee as specified in the organization’s QMP',
      'non_epa_op_man': 'Signature of the non-EPA Operations Manager',
      'non_epa_qam': 'Signature of the non-EPA Project QAM or an individual from the non-EPA organization with QA responsibilities for the project',
      'supervisor': 'Signature from direct line supervisor of the EPA Operations Manager',
      'pqapp_dir': 'Programmatic QAPPs (PQAPPs), signature of Center/Office Director of QA',
    }

    def __init__(self, *args, **kwargs):
      super(SectionA2Form, self).__init__(*args, **kwargs)

# class SectionA3Form(EpaBaseForm):
#   """Form for Section A3."""

#   class Meta:
#     model = SectionA3
#     exclude = ['section_a', 'qapp']

#     def __init__(self, *args, **kwargs):
#       super(SectionA3Form, self).__init__(*args, **kwargs)

class SectionA4Form(EpaBaseForm):
  """Form for Section A4."""

  class Meta:
    model = SectionA4
    exclude = ['section_a', 'qapp']
    labels = {
      'backgroun_desc': 'Describe and/or cite background information, plans, and/or reports to provide the historical, scientific, and regulatory perspective for the project',
      'existing_sources': 'Identify the sources for existing information for the project',
      'other_docs': 'Identify and address other QA planning documents that have relevant requirements such as QMPs, programmatic QAPPs, etc',
      'eio_purpose': 'Describe the purpose of the project’s EIO ',
      'env_decisions': 'Describe the environmental decision(s)',
      'needed_info': 'Identify the type, quantity, and quality of information needed for its intended use, and describe the acceptance and performance criteria.',
    }

    def __init__(self, *args, **kwargs):
      super(SectionA4Form, self).__init__(*args, **kwargs)