from django import forms
from qapp_builder.models import Qapp


class QappForm(forms.ModelForm):
  class Meta:
    model = Qapp
    fields = ['title', 'teams']

  def __init__(self, *args, **kwargs):
    super(QappForm, self).__init__(*args, **kwargs)
    self.fields['created_by'].widget = forms.HiddenInput()
