from .utility_forms import EpaBaseForm
from qapp_builder.models import SectionC, SectionD


class SectionCForm(EpaBaseForm):

    class Meta:
        model = SectionC
        exclude = ['qapp']
        labels = SectionC().labels


class SectionDForm(EpaBaseForm):

    class Meta:
        model = SectionD
        exclude = ['qapp']
        labels = SectionD().labels
