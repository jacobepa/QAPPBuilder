from django import forms
from qapp_builder.models import SectionA1, SectionA2, SectionA4, SectionA10, \
    SectionA5, SectionA6, SectionA11, \
    AdditionalSignature, AcronymAbbreviation, Distribution, \
    RoleResponsibility, DocumentRecord
from .utility_forms import EpaBaseForm
from constants.qapp_section_a_const import SECTION_A


class SectionA1Form(EpaBaseForm):

    class Meta:
        model = SectionA1
        exclude = ['qapp']
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
        # labels = SECTION_A['a1']['labels']
        labels = SectionA1().labels

    def __init__(self, *args, **kwargs):
        super(SectionA1Form, self).__init__(*args, **kwargs)
        self.fields['accessibility'].widget = forms.CheckboxInput(attrs={
            'class': 'usa-checkbox__input',
            'id': 'accessibility-checkbox'
        })


class SectionA2Form(EpaBaseForm):

    class Meta:
        model = SectionA2
        exclude = ['qapp']
        labels = SectionA2().labels


class AdditionalSignatureForm(EpaBaseForm):

    class Meta:
        model = AdditionalSignature
        exclude = ['section_a2']


# NOTE: No Section A3 form. Revisions and Acronyms/Abbreviations/Definitions
# class SectionA3Form(EpaBaseForm):


class AcronymAbbreviationForm(EpaBaseForm):

    class Meta:
        model = AcronymAbbreviation
        exclude = ['qapp']
        labels = AcronymAbbreviation().labels


class SectionA4Form(EpaBaseForm):

    class Meta:
        model = SectionA4
        exclude = ['qapp']
        # labels = SECTION_A['a4']['labels']


class SectionA5Form(EpaBaseForm):

    class Meta:
        model = SectionA5
        exclude = ['qapp']
        labels = SECTION_A['a5']['labels']


class SectionA6Form(EpaBaseForm):

    class Meta:
        model = SectionA6
        exclude = ['qapp']
        labels = SECTION_A['a6']['labels']


class DistributionForm(EpaBaseForm):

    class Meta:
        model = Distribution
        exclude = ['qapp_id', 'qapp']
        labels = Distribution().labels


class RoleResponsibilityForm(EpaBaseForm):

    class Meta:
        model = RoleResponsibility
        exclude = ['qapp_id', 'qapp']
        labels = RoleResponsibility().labels


class SectionA10Form(EpaBaseForm):

    class Meta:
        model = SectionA10
        exclude = ['qapp']
        labels = {'org_chart': 'Organization Chart File Upload'}
        widgets = {
            'org_chart': forms.FileInput(attrs={'class': 'usa-file-input'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['org_chart'].widget.attrs.update({
            'accept': 'image/*,.pdf,.doc,.docx'  # Accept common file types
        })


class SectionA11Form(EpaBaseForm):

    class Meta:
        model = SectionA11
        exclude = ['qapp']
        # labels = SECTION_A['a11']['labels']


class DocumentRecordForm(EpaBaseForm):

    class Meta:
        model = DocumentRecord
        exclude = ['qapp_id', 'qapp']
        labels = DocumentRecord().labels
