from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
# from django_select2.forms import ModelSelect2MultipleWidget
from qapp_builder.models import SectionA1, VersionControl, Definition


class SectionA1Form(forms.ModelForm):
  versions = forms.ModelMultipleChoiceField(
    queryset=VersionControl.objects.all(),
    widget=FilteredSelectMultiple("Your Field Label", is_stacked=False),
    required=False
  )
  definitions = forms.ModelMultipleChoiceField(
    queryset=Definition.objects.all(),
    widget=FilteredSelectMultiple("Your Field Label", is_stacked=False),
    required=False
  )

  # versions = forms.ModelMultipleChoiceField(
  #   queryset=VersionControl.objects.all(),
  #   # widget=forms.SelectMultiple,
  #   widget=ModelSelect2MultipleWidget(model=VersionControl),
  #   required=False
  # )
  # definitions = forms.ModelMultipleChoiceField(
  #   queryset=Definition.objects.all(),
  #   # widget=forms.SelectMultiple,
  #   widget=ModelSelect2MultipleWidget(model=Definition),
  #   required=False
  # )

  class Meta:
    model = SectionA1
    fields = '__all__'

  class Media:
    css = {'all': ('/static/admin/css/widgets.css',)}
    js = ('/admin/js/core.js', '/admin/js/SelectBox.js',
          '/admin/js/SelectFilter2.js')
