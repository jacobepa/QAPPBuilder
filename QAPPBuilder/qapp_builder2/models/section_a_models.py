from django.db import models
from qapp_builder2.models.utility_models import VersionControl, Definition, \
  Participant, QappDocument


class SectionA1(models.Model):
  """Section A1 is the QAPP's Title Page"""

  # ###########################################################################
  # Required for both EPA and non-EPA orgs:
  # ---------------------------------------
  title = models.TextField(blank=False, null=False)
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


class SectionA2(models.Model):
  """
  Section A2 is the QAPP's Approval Page.

  Note that these are all signature inputs, so for the Django app, the user
  should record the names of those who will eventually sign the document.

  When the QAPP is printed to docx or PDF, we will need insert signature lines
  above each expected signature in Section A2.
  """

  # Required for all organizations (EPA and Non-EPA)
  epa_op_man = models.TextField(blank=False, null=False)
  epa_qam = models.TextField(blank=False, null=False)

  # Required for non-EPA organizations
  non_epa_op_man = models.TextField(blank=True, null=True)
  non_epa_qam = models.TextField(blank=True, null=True)

  # Additional ORD QAPP Requirements
  supervisor = models.TextField(blank=True, null=True)
  pqapp_dir = models.TextField(blank=True, null=True)


# class SectionA3(models.Model):
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


class SectionA4(models.Model):
  """A4: Project Purpose, Problem Definition and Background"""

  # A4.1: Project Background
  f1 = models.TextField()
  f2 = models.TextField()
  f3 = models.TextField()

  # A4.2: Project Purpose and Problem Definition
  f4 = models.TextField()
  f5 = models.TextField()
  f6 = models.TextField()


class SectionA5(models.Model):
  """A5: Project Task Description"""

  desc = models.TextField()
  deliverables = models.TextField()
  tasks_and_sched = models.TextField()

  # Social Sciences only:
  irb_review = models.TextField()
  irb_exception = models.TextField()

  # Software and Application Development only:
  ord_app_inv_entry = models.TextField()


class SectionA6(models.Model):
  """
  A6: Information/Data Quality Objectives and Performance/Acceptance Criteria
  """

  dqo = models.TextField()
  criteria = models.TextField()
  dqi = models.TextField()


class SectionA7(models.Model):
  """A7: Distribution List"""

  distributor = models.TextField()
  # recipients = models.TextField()
  distribution_list = models.ManyToManyField(Participant)


class SectionA8(models.Model):
  """A8: Project Organization"""

  # TODO: The participant list is related to the distribution list above
  #       I actually think it is the same list, but they want an org chart here
  # participant_list = models.ManyToManyField(Participant)
  org_chart = models.ImageField()
  qam_oversight = models.TextField()
  qam_authority = models.TextField()

  # Software and Application Development only:
  a_team_rep = models.TextField()


class SectionA9(models.Model):
  """A9: Project Quality Assurance Manager Independence"""

  desc = models.TextField()


class SectionA10(models.Model):
  """A10: Project Organization Chart and Communications"""

  # TODO is project org chart an image or table?
  proj_org_chart = models.ImageField()
  comms_desc = models.TextField()
  comm_procedures = models.TextField()

  # Non-EPA only:
  non_epa_comms = models.TextField()


class SectionA11(models.Model):
  """A11: Personnel Training/Certification"""

  eio_verifier = models.TextField()
  training_documenter = models.TextField()
  spec_training_certs = models.TextField()
  training_eval = models.TextField()

  # Field Activities only:
  training_reqs = models.TextField()

  # Social Sciences only:
  citi_personnel = models.TextField()


class SectionA12(models.Model):
  """A12: Documents and Records"""

  # TODO: Check format of documents and records
  docs_records = models.ManyToManyField(QappDocument)
  requirements = models.TextField()
  record_sched = models.TextField()

  # Field Activities only:
  dc_rm_reqs = models.TextField()
  citation = models.TextField()


class SectionA(models.Model):

  a1 = models.ForeignKey(SectionA1, on_delete=models.CASCADE)
  a2 = models.ForeignKey(SectionA2, on_delete=models.CASCADE)
  # NOTE: A3 doesn't have any inputs...
  a4 = models.ForeignKey(SectionA4, on_delete=models.CASCADE)
  a5 = models.ForeignKey(SectionA5, on_delete=models.CASCADE)
  a6 = models.ForeignKey(SectionA6, on_delete=models.CASCADE)
  a7 = models.ForeignKey(SectionA7, on_delete=models.CASCADE)
  a8 = models.ForeignKey(SectionA8, on_delete=models.CASCADE)
  a9 = models.ForeignKey(SectionA9, on_delete=models.CASCADE)
  a10 = models.ForeignKey(SectionA10, on_delete=models.CASCADE)
  a11 = models.ForeignKey(SectionA11, on_delete=models.CASCADE)
  a12 = models.ForeignKey(SectionA12, on_delete=models.CASCADE)
