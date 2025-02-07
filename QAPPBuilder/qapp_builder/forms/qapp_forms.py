from django import forms
from qapp_builder.models import Qapp
from teams.models import Team


class QappForm(forms.ModelForm):

  teams = forms.ModelMultipleChoiceField(
    widget=forms.SelectMultiple({'class': 'form-control mb-2',
                                 'placeholder': 'Teams'}),
    queryset=Team.objects.all(),
    label="Share With Teams", required=False)

  class Meta:
    model = Qapp
    fields = ['title', 'teams']

  # def __init__(self, *args, **kwargs):
  #   super(QappForm, self).__init__(*args, **kwargs)
  #   self.fields['created_by'].widget = forms.HiddenInput()
