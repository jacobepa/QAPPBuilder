from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
# from django.forms.models import inlineformset_factory
from qapp_builder.models import SectionA1, VersionControl, Definition


class SectionA1Form(forms.ModelForm):
  class Meta:
    model = SectionA1
    fields = '__all__'

  # Use FilteredSelectMultiple for ManyToManyField
  versions = forms.ModelMultipleChoiceField(
    queryset=VersionControl.objects.all(),
    widget=FilteredSelectMultiple("Versions", is_stacked=False),
  )

  definitions = forms.ModelMultipleChoiceField(
    queryset=Definition.objects.all(),
    widget=FilteredSelectMultiple("Definitions", is_stacked=False),
    required=False,
  )

  # Adding an inline formset for creating new Definitions
  def __init__(self, *args, **kwargs):
    super(SectionA1Form, self).__init__(*args, **kwargs)
    self.fields['new_definitions'] = forms.CharField(
      required=False,
      widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}),
      help_text='Add new definitions here, separated by commas'
    )

  def save(self, commit=True):
    instance = super(SectionA1Form, self).save(commit=False)
    if commit:
      instance.save()
      self.save_m2m()  # Save ManyToMany relations

      # Process new definitions
      new_definitions = self.cleaned_data.get('new_definitions', '').strip()
      if new_definitions:
        for definition in new_definitions.split(','):
          acronym_abbrev, definition_text = definition.split(':')
          new_def = Definition.objects.create(
            acronym_abbrev=acronym_abbrev.strip(),
            definition=definition_text.strip()
          )
          instance.definitions.add(new_def)

    return instance
