from django.db import models
from .qapp_models import Qapp
from .utility_models import EpaBaseModel


class SectionB(EpaBaseModel):

  qapp = models.OneToOneField(
    Qapp, on_delete=models.CASCADE, related_name='section_b')
  discipline = models.TextField(null=True, blank=True)


class SectionB1(EpaBaseModel):
  """
  Section B1: Identification of Project Environmental Information Operations
  """

  section_b = models.OneToOneField(
    SectionB, on_delete=models.CASCADE, related_name='section_b1')
  eio = models.TextField(null=False, blank=False)
  proj_purpose = models.TextField(null=False, blank=False)
  performance_acceptance = models.TextField(null=False, blank=False)


class SectionB2(EpaBaseModel):
  """
  Section B2:
  """

  section_b = models.OneToOneField(
    SectionB, on_delete=models.CASCADE, related_name='section_b2')
