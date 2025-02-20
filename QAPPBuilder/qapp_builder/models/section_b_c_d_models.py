from django.db import models
from .qapp_models import Qapp
from .utility_models import EpaBaseModel


class SectionB(EpaBaseModel):

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, related_name='section_b')
    b1 = models.TextField(blank=False, null=False)
    b2 = models.TextField(blank=False, null=False)
    b3 = models.TextField(blank=False, null=False)
    b4 = models.TextField(blank=False, null=False)
    b5 = models.TextField(blank=False, null=False)
    b6 = models.TextField(blank=False, null=False)
    # b7 = models.TextField(blank=False, null=False)
    b7_1 = models.TextField(blank=False, null=False)
    b7_2 = models.TextField(blank=False, null=False)
    b7_3 = models.TextField(blank=False, null=False)
    # B7.3 Includes Table 6:
    # Table 6. Required Hardware, Operating System, and Types of
    #          Specialized Software for EIO
    # B7.4 is readonly.
    # b7_4 = models.TextField(blank=False, null=False)


class HardwareSoftware(EpaBaseModel):

    hardware = models.TextField(blank=False, null=False)
    os = models.TextField(blank=True, null=True)
    # NOTE: Details include... Non-Microsoft Office Software and
    #                          Version/Special Performance Requirements/Use
    details = models.TextField(blank=True, null=True)


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
