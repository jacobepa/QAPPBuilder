from django import forms
from qapp_builder.models import SectionA1, SectionA2, SectionA3, SectionA4, \
    SectionA5, SectionA6, SectionA7, SectionA8, SectionA11, SectionA12
from .utility_forms import EpaBaseForm


class SectionA1Form(EpaBaseForm):

    class Meta:
        model = SectionA1
        exclude = ['section_a', 'qapp']
        widgets = {
            # TODO: These need to be selectable...
            # 'ord_center': forms.Select(attrs={'class': 'usa-select'}),
            # 'division': forms.Select(attrs={'class': 'usa-select'}),
            # 'branch': forms.Select(attrs={'class': 'usa-select'}),
            # 'ord_national_program': forms.Select(
            #     attrs={'class': 'usa-select'}),
            'version_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'type': 'date', 'class': 'usa-input'}),
            'qa_category': forms.Select(attrs={'class': 'usa-select'}),
            'intra_or_extra': forms.Select(attrs={'class': 'usa-select'}),
            # 'accessibility': forms.CheckboxInput(
            #     attrs={'class': 'usa-checkbox'}),
            'disciplines': forms.SelectMultiple(attrs={'class': 'usa-select'}),
        }

    def __init__(self, *args, **kwargs):
        super(SectionA1Form, self).__init__(*args, **kwargs)
        self.fields['accessibility'].widget = forms.CheckboxInput(attrs={
            'class': 'usa-checkbox__input',
            'id': 'accessibility-checkbox'
        })


class SectionA2Form(EpaBaseForm):

    class Meta:
        model = SectionA2
        exclude = ['section_a', 'qapp']


class SectionA3Form(EpaBaseForm):

    class Meta:
        model = SectionA3
        exclude = ['section_a', 'qapp']


class SectionA4Form(EpaBaseForm):

    class Meta:
        model = SectionA4
        exclude = ['section_a', 'qapp']


class SectionA5Form(EpaBaseForm):

    class Meta:
        model = SectionA5
        exclude = ['section_a', 'qapp']


class SectionA6Form(EpaBaseForm):

    class Meta:
        model = SectionA6
        exclude = ['section_a', 'qapp']


class SectionA7Form(EpaBaseForm):

    class Meta:
        model = SectionA7
        exclude = ['section_a', 'qapp']


class SectionA8Form(EpaBaseForm):

    class Meta:
        model = SectionA8
        exclude = ['section_a', 'qapp']


class SectionA11Form(EpaBaseForm):

    class Meta:
        model = SectionA11
        exclude = ['section_a', 'qapp']


class SectionA12Form(EpaBaseForm):

    class Meta:
        model = SectionA12
        exclude = ['section_a', 'qapp']
