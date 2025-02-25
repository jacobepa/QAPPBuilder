from django import forms
from .utility_forms import EpaBaseForm
from qapp_builder.models import Qapp, Revision
from teams.models import Team


class QappForm(EpaBaseForm):
    teams = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'usa-select'}),
        queryset=Team.objects.all(),
        label="Share With Teams", required=False)

    class Meta:
        model = Qapp
        fields = ['title', 'teams']


class RevisionForm(EpaBaseForm):

    class Meta:
        model = Revision
        fields = ['date', 'author', 'description']

        widgets = {
            'date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'type': 'date', 'class': 'usa-input'})
        }
