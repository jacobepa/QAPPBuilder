from django.db import models
from .qapp_models import Qapp
from .utility_models import EpaBaseModel


#
class SectionB2A1Model(EpaBaseModel):
  """
  2.A.1 Experimental Process
  Measurement and Monitoring (Field/Lab) Requirements for Section 2 of the
  ORD Discipline Specific QAPP Template
  """

  # All Measurement and Monitoring Activities
  rationale_desc = models.TextField()
  max_hold_time = models.TextField()
  limitations = models.TextField()

  # 2.A.2 Sample Collection and Management
