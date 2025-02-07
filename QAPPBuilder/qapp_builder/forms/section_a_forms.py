from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from qapp_builder.models import SectionA1, SectionA2, VersionControl, Definition
from .utility_forms import as_epa, assign_epa_css


class SectionA1Form(forms.ModelForm):
  class Meta:
    model = SectionA1
    fields = '__all__'
    widgets = {
      'versions': FilteredSelectMultiple("Versions", is_stacked=False),
      'definitions': FilteredSelectMultiple("Definitions", is_stacked=False),
    }

  def __init__(self, *args, **kwargs):
    super(SectionA1Form, self).__init__(*args, **kwargs)
    self.fields['versions'].queryset = VersionControl.objects.all()
    self.fields['definitions'].queryset = Definition.objects.all()
    assign_epa_css(self)

  def as_epa(self):
    return as_epa(self)


class SectionA2Form(forms.ModelForm):
  class Meta:
    model = SectionA2
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(SectionA2Form, self).__init__(*args, **kwargs)
    assign_epa_css(self)

  def as_epa(self):
    return as_epa(self)
