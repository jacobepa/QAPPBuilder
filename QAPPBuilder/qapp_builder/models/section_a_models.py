from django.db import models
from .qapp_models import Qapp
from .utility_models import (
  VersionControl, Definition, Participant, QappDocument, EpaTemplateModel
)


class SectionA(EpaTemplateModel):

  qapp = models.OneToOneField(
    Qapp, on_delete=models.CASCADE, related_name='section_a')


class SectionA1(EpaTemplateModel):
  """Section A1 is the QAPP's Title Page"""

  section_a = models.OneToOneField(
    SectionA, on_delete=models.CASCADE, related_name='section_a1')

  # ###########################################################################
  # Required for both EPA and non-EPA orgs:
  # ---------------------------------------
  # NOTE: Moved title to the QAPP object instead.
  # title = models.TextField(blank=False, null=False)
  version_date = models.DateField(blank=False, null=False)
  # Name of the org conducting the environmental information operations
  conducting_org_name = models.TextField(blank=False, null=False)
  # Name of the org that developed the QAPP (if different from conducting)
  developing_org_name = models.TextField(blank=False, null=False)
  applicability_period = models.TextField(blank=False, null=False)
  # Allow many to many for version control info
  versions = models.ManyToManyField(VersionControl)
  # TODO: This should probably be selector with option to add new?
  doc_control_identifier = models.TextField(blank=False, null=False)
  # ###########################################################################
  # Non-EPA orgs only:
  # ------------------
  # Grant or cooperative agreement number if the work is being performed under
  # an EPA assistance agreement.
  agreement_num = models.TextField(blank=True, null=True)
  # Contract number and Task Order (TO) number if the work is being performed
  # under an acquisition.
  con_to_num = models.TextField(blank=True, null=True)
  # Interagency agreement number if the work is being performed under an
  # interagency agreement (IA).
  ia_num = models.TextField(blank=True, null=True)
  # Title and date of Memorandum of Understanding (MOU)/Agreement
  mou_title = models.TextField(blank=True, null=True)
  mou_date = models.DateField(blank=True, null=True)
  # Citation of the regulatory requirement, if applicable
  reg_req_cit = models.TextField(blank=True, null=True)
  # Title and date of the enforcement or legal agreement, if applicable
  enf_legal_title = models.TextField(blank=True, null=True)
  enf_legal_date = models.DateField(blank=True, null=True)
  # ###########################################################################
  # Additional ORD QAPP Requirements:
  # ---------------------------------
  ord_qa_cat = models.TextField(blank=True, null=True)
  ord_program = models.TextField(blank=True, null=True)
  definitions = models.ManyToManyField(Definition)
  # ###########################################################################


class SectionA2(EpaTemplateModel):
  """
  Section A2 is the QAPP's Approval Page.

  Note that these are all signature inputs, so for the Django app, the user
  should record the names of those who will eventually sign the document.

  When the QAPP is printed to docx or PDF, we will need insert signature lines
  above each expected signature in Section A2.
  """

  section_a = models.OneToOneField(
    SectionA, on_delete=models.CASCADE, related_name='section_a2')

  # Required for all organizations (EPA and Non-EPA)
  epa_op_man = models.TextField(blank=False, null=False)
  epa_qam = models.TextField(blank=False, null=False)

  # Required for non-EPA organizations
  non_epa_op_man = models.TextField(blank=True, null=True)
  non_epa_qam = models.TextField(blank=True, null=True)

  # Additional ORD QAPP Requirements
  supervisor = models.TextField(blank=True, null=True)
  pqapp_dir = models.TextField(blank=True, null=True)


# class SectionA3(EpaTemplateModel):
#   """
#   Section A3 is the QAPP's Table of Contents, Document Format,
#   and Document Control.

#   A3 seems less like a dedicated section and more like guidance for
#   maintaining the document as a whole...
#   """

#   # table_of_contents
#   # revision_history_page/table
#   # format complies
#   # Document control information is included on every page and includes:
#     # o Title of the document (abbreviations and acronyms are acceptable)
#     # o Version number of the document (included in the ORD QA Track ID)
#     # o Date of the version
#     # o Page number in relation to the total number of pages (i.e., pg X of Y)


class SectionA4(EpaTemplateModel):
  """A4: Project Purpose, Problem Definition and Background"""

  section_a = models.OneToOneField(
    SectionA, on_delete=models.CASCADE, related_name='section_a4')

  # A4.1: Project Background
  backgroun_desc = models.TextField()
  existing_sources = models.TextField()
  other_docs = models.TextField()

  # A4.2: Project Purpose and Problem Definition
  eio_purpose = models.TextField()
  env_decisions = models.TextField()
  needed_info = models.TextField()


class SectionA5(EpaTemplateModel):
  """A5: Project Task Description"""

  section_a = models.OneToOneField(
    SectionA, on_delete=models.CASCADE, related_name='section_a5')

  desc = models.TextField()
  deliverables = models.TextField()
  tasks_and_sched = models.TextField()

  # Social Sciences only:
  irb_review = models.TextField()
  irb_exception = models.TextField()

  # Software and Application Development only:
  ord_app_inv_entry = models.TextField()


class SectionA6(EpaTemplateModel):
  """
  A6: Information/Data Quality Objectives and Performance/Acceptance Criteria
  """

  section_a = models.OneToOneField(
    SectionA, on_delete=models.CASCADE, related_name='section_a6')

  dqo = models.TextField()
  criteria = models.TextField()
  dqi = models.TextField()


class SectionA7(EpaTemplateModel):
  """A7: Distribution List"""

  section_a = models.OneToOneField(
    SectionA, on_delete=models.CASCADE, related_name='section_a7')

  distributor = models.TextField()
  # recipients = models.TextField()
  distribution_list = models.ManyToManyField(Participant)


class SectionA8(EpaTemplateModel):
  """A8: Project Organization"""

  section_a = models.OneToOneField(
    SectionA, on_delete=models.CASCADE, related_name='section_a8')

  # TODO: The participant list is related to the distribution list above
  #       I actually think it is the same list, but they want an org chart here
  # participant_list = models.ManyToManyField(Participant)
  org_chart = models.ImageField()
  qam_oversight = models.TextField()
  qam_authority = models.TextField()

  # Software and Application Development only:
  a_team_rep = models.TextField()


class SectionA9(EpaTemplateModel):
  """A9: Project Quality Assurance Manager Independence"""

  section_a = models.OneToOneField(
    SectionA, on_delete=models.CASCADE, related_name='section_a9')

  desc = models.TextField()


class SectionA10(EpaTemplateModel):
  """A10: Project Organization Chart and Communications"""

  section_a = models.OneToOneField(
    SectionA, on_delete=models.CASCADE, related_name='section_a10')

  # TODO is project org chart an image or table?
  proj_org_chart = models.ImageField()
  comms_desc = models.TextField()
  comm_procedures = models.TextField()

  # Non-EPA only:
  non_epa_comms = models.TextField()


class SectionA11(EpaTemplateModel):
  """A11: Personnel Training/Certification"""

  section_a = models.OneToOneField(
    SectionA, on_delete=models.CASCADE, related_name='section_a11')

  eio_verifier = models.TextField()
  training_documenter = models.TextField()
  spec_training_certs = models.TextField()
  training_eval = models.TextField()

  # Field Activities only:
  training_reqs = models.TextField()

  # Social Sciences only:
  citi_personnel = models.TextField()


class SectionA12(EpaTemplateModel):
  """A12: Documents and Records"""

  section_a = models.OneToOneField(
    SectionA, on_delete=models.CASCADE, related_name='section_a12')

  # TODO: Check format of documents and records
  docs_records = models.ManyToManyField(QappDocument)
  requirements = models.TextField()
  record_sched = models.TextField()

  # Field Activities only:
  dc_rm_reqs = models.TextField()
  citation = models.TextField()
