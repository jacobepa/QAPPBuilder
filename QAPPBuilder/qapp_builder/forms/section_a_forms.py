# from django import forms
# from django.contrib.admin.widgets import FilteredSelectMultiple
from qapp_builder.models import SectionA1
from .utility_forms import EpaBaseForm


class SectionA1Form(EpaBaseForm):

    class Meta:
        model = SectionA1
        exclude = ['section_a', 'qapp']
        # widgets = {
        #     'version_date': forms.DateInput(format='%Y-%m-%d', attrs={
        #         'type': 'date', 'class': 'usa-input'}),
        #     'mou_date': forms.DateInput(format='%Y-%m-%d', attrs={
        #         'type': 'date', 'class': 'usa-input'}),
        #     'enf_legal_date': forms.DateInput(format='%Y-%m-%d', attrs={
        #         'type': 'date', 'class': 'usa-input'}),
        # }
