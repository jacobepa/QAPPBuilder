from django.db import models
from .qapp_models import Qapp
from .utility_models import EpaBaseModel
from constants.qapp_section_b_const import SECTION_B


class SectionB(EpaBaseModel):

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, related_name='section_b')
    b1 = models.TextField(blank=False, null=False)
    b2 = models.TextField(blank=False, null=False)
    b3 = models.TextField(blank=False, null=False)
    b4 = models.TextField(blank=False, null=False)
    b5 = models.TextField(blank=False, null=False)
    b6 = models.TextField(blank=False, null=False)

    @property
    def labels(self):
        return {
            'b1': SECTION_B['b1']['header'],
            'b2': SECTION_B['b2']['header'],
            'b3': SECTION_B['b3']['header'],
            'b4': SECTION_B['b4']['header'],
            'b5': SECTION_B['b5']['header'],
            'b6': SECTION_B['b6']['header']
        }


class SectionB7(EpaBaseModel):

    qapp = models.OneToOneField(Qapp, on_delete=models.CASCADE)
    b71 = models.TextField(blank=False, null=False)
    b72 = models.TextField(blank=False, null=False)
    # B7.3 Includes Table 6:
    # Table 6. Required Hardware, Operating System, and Types of
    #          Specialized Software for EIO
    # b73 = models.TextField(blank=False, null=False)
    # B7.4 is readonly.
    # b74 = models.TextField(blank=False, null=False)

    @property
    def labels(self):
        return {
            'b7': SECTION_B['b7']['header'],
            'b71': SECTION_B['b71']['header'],
            'b72': SECTION_B['b72']['header'],
            'b73': SECTION_B['b73']['header'],
            'b74': SECTION_B['b74']['header']
        }


class HardwareSoftware(EpaBaseModel):

    qapp = models.ForeignKey(Qapp, on_delete=models.CASCADE)
    hardware = models.TextField(blank=False, null=False)
    os = models.TextField(blank=True, null=True)
    # NOTE: Details include... Non-Microsoft Office Software and
    #                          Version/Special Performance Requirements/Use
    details = models.TextField(blank=True, null=True)

    @property
    def labels(self):
        return {
            'hardware': 'Hardware',
            'os': 'Operating System',
            'details': 'Non-Microsoft Office Software and Version/Special '
            'Performance Requirements/Use',
        }


class SectionC(EpaBaseModel):

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, related_name='section_c')
    # Section C1, C1.1, C1.2 are all readonly
    c2 = models.TextField(blank=False, null=False)


class SectionD(EpaBaseModel):

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, related_name='section_d')
    d1 = models.TextField(blank=False, null=False)
    d2 = models.TextField(blank=False, null=False)
