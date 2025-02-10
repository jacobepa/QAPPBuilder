from django import forms
from .utility_forms import as_epa, assign_epa_css
from qapp_builder.models import Qapp
from teams.models import Team


class QappForm(forms.ModelForm):
  teams = forms.ModelMultipleChoiceField(
    widget=forms.SelectMultiple(attrs={'class': 'usa-select'}),
    queryset=Team.objects.all(),
    label="Share With Teams", required=False)

  class Meta:
    model = Qapp
    fields = ['title', 'teams']

  def __init__(self, *args, **kwargs):
    super(QappForm, self).__init__(*args, **kwargs)
    assign_epa_css(self)

  def as_epa(self):
    return as_epa(self)
