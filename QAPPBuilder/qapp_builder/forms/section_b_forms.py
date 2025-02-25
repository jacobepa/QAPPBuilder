# from django import forms
from qapp_builder.models import SectionB, SectionB7, HardwareSoftware
from .utility_forms import EpaBaseForm
# from constants.qapp_section_a_const import SECTION_B


class SectionBForm(EpaBaseForm):

    class Meta:
        model = SectionB
        exclude = ['qapp']
        labels = SectionB().labels


class SectionB7Form(EpaBaseForm):

    class Meta:
        model = SectionB7
        exclude = ['qapp', 'b73', 'b74']
        labels = SectionB7().labels


class HardwareSoftwareForm(EpaBaseForm):

    class Meta:
        model = HardwareSoftware
        exclude = ['qapp']
        labels = HardwareSoftware().labels
