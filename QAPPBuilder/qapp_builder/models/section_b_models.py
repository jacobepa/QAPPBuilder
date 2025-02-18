from django.db import models
from constants import section_b_const as con
from .qapp_models import Qapp
from .utility_models import EpaBaseModel


# class SectionBStandard(EpaBaseModel):
#   """Inputs for a Standard section B, i.e. no discipline(s) selected."""

#   a_field = models.TextField(null=False, blank=False)


class EquipmentSection(EpaBaseModel):

  # B5: Instruments/Equipment Calibration, Testing, Inspection, and Maintenance
  # Field, Laboratory and/or Environmental Technology Activities ONLY
  equipment_used = models.TextField()
  equipment_procedures_docs = models.TextField()
  equipment_calibration = models.TextField()
  equipment_testing_maint = models.TextField()
  spare_parts = models.TextField()
  # TODO: Table B-7. Example Equipment and Instrument Maintenance, Testing,
  #                  and Inspection and Calibration
  # TODO: Table B-8. Example Equipment and Instrument Inspection and
  #                  Calibration Table


class FieldLabSection(EpaBaseModel):

  # B4.Field/LabActivities (not Env Tech?)
  field_lab_qc_desc = models.TextField()
  # B6: Inspection/Acceptance of Supplies and Services
  # Lab and Field Supplies -- MOVED TO LAB/FIELD ABSTRACT CLASS
  supply_personnel = models.TextField()
  supplies_to_inspect = models.TextField()
  inspection_procedures = models.TextField()
  acceptance_doc = models.TextField()

  class Meta:
    abstract = True


class SectionB(EpaBaseModel):
  """
  Section B for a QAPP that can include one or more selected disciplines
  via cross-reference class SectionBDisciplines
  """

  qapp = models.OneToOneField(
    Qapp, on_delete=models.CASCADE, related_name='section_b')
  # standard_inputs = models.OneToOneField(SectionBStandard,
  #                                        on_delete=models.CASCADE)
  # ###########################################################################
  # B1: Identification of Project Environmental Information Operations
  eio_detail = models.TextField()
  proj_purpose = models.TextField()
  perf_criteria = models.TextField()
  # ---------------------------------------------------------------------------
  # B2: Methods for Environmental Information Acquisition
  methods_procedures = models.TextField()
  methods_specifics = models.TextField()
  sops_env_info_acquisition = models.TextField()
  # TODO: Table B-1. Example SOP Details for this Project
  # TODO: Table B-2. Example Field Sampling Table
  # ---------------------------------------------------------------------------
  # B3: Integrity of Environmental Information
  integrity_procedures = models.TextField()
  # ---------------------------------------------------------------------------
  # B4: Quality Control
  qc_activities = models.TextField()
  qc_frequency = models.TextField()
  statistics_procedures = models.TextField()
  # TODO: In the PDF guidance, they show tables of QC Check/Info:
  #       "Table B-5. Project Quality Control Checks"
  #       "Table B-6. Example QC X Table"
  # ---------------------------------------------------------------------------
  # B5: Instruments/Equipment Calibration, Testing, Inspection, and Maintenance
  # MOVED TO EQUIPMENT SECTION
  # ---------------------------------------------------------------------------
  # B6: Inspection/Acceptance of Supplies and Services
  # Lab and Field Supplies -- MOVED TO FIELD/LAB ABSTRACT CLASS
  # Vendor Services
  services_personnel = models.TextField()
  services_provided = models.TextField()
  services_procedures = models.TextField()
  services_doc = models.TextField()
  vendor_qapp_elements = models.TextField()
  vendor_qapp_adherence = models.TextField()
  # ---------------------------------------------------------------------------
  # B7: Environmental Information Management
  # --- B7.1: Information Handling and Storage
  env_info_managment_proc = models.TextField()
  doc_procedures = models.TextField()
  info_processing_procedures = models.TextField()
  # --- B7.2: Information Security
  # data_control = models.TextField()
  # NOTE: This section has one primary field with four sub-bullets...
  data_transference = models.TextField()
  perm_retention_conversion = models.TextField()
  data_special_agreements = models.TextField()
  data_forms_checklists = models.TextField()
  # --- B7.3: Information Systems
  # Document hardware, software, and performance requirements:
  specialized_hardware = models.TextField()
  specialized_software = models.TextField()
  config_procedures = models.TextField()
  # TODO: Table 6. Req Hardware, OS, and Types of Specialized Software for EIO
  # --- B7.4: Information Accessibility
  public_data_preservation = models.TextField()
  # ---------------------------------------------------------------------------


class SectionBDisciplines(EpaBaseModel):
  """
  Cross-reference class for mapping multiple selected disciplines to a
  QAPP's Section B.
  """

  section_b = models.ForeignKey(SectionB, on_delete=models.CASCADE)
  discipline = models.TextField(
    choices=con.DISCIPLINE_CHOICES, null=False, blank=False)


class FieldActivity(FieldLabSection):
  """
  Section B: Standard subsection for Field Activity.
  This technically is part of the Standard template and is not
  discipline-specific. However, for model and code organization, it makes
  sense to separate it out into its own model.
  """

  section_b = models.ForeignKey(SectionB, on_delete=models.CASCADE)
  # B2.FieldActivities
  field_procedures = models.TextField()
  field_description = models.TextField()
  # B3.FieldActivities
  field_sample_custody = models.TextField()
  field_labels_and_logs = models.TextField()
  # TODO: Table B-9. Example Inspection/Acceptance Testing Requirements for
  #                  Consumables and Supplies


class LaboratoryActivity(FieldLabSection):
  """
  Section B: Standard subsection for Laboratory Activity.
  This technically is part of the Standard template and is not
  discipline-specific. However, for model and code organization, it makes
  sense to separate it out into its own model.
  """

  section_b = models.ForeignKey(SectionB, on_delete=models.CASCADE)
  # B2.LaboratoryActivities
  lab_analytical_methods = models.TextField()
  lab_sops = models.TextField()
  lab_turnaround_time = models.TextField()
  lab_method_information = models.TextField()
  # TODO: Table B-3. Example Analytical Methods Table
  # TODO: Table B-9. Example Inspection/Acceptance Testing Requirements for
  #                  Consumables and Supplies
  # B3.LabActivities
  lab_laboratories_list = models.TextField()
  lab_laboratories_accred = models.TextField()


class MeasurementMonitoring(EpaBaseModel):
  """Section B: Measurement and Monitoring specific inputs."""

  section_b = models.ForeignKey(SectionB, on_delete=models.CASCADE)


class EnvironmentalTechnology(EpaBaseModel):
  """Section B: Environmental Technology specific inputs."""

  section_b = models.ForeignKey(SectionB, on_delete=models.CASCADE)


class ExistingData(EpaBaseModel):
  """Section B: Existing Data specific inputs."""

  section_b = models.ForeignKey(SectionB, on_delete=models.CASCADE)
  # TODO: Table B-4. Existing Data for Addressing Research
  #                  Questions & Data Limitations


class ModelApplicationEvaluation(EpaBaseModel):
  """Section B: Model Application and Evaluation specific inputs."""

  section_b = models.ForeignKey(SectionB, on_delete=models.CASCADE)


class CodeBasedModeling(EpaBaseModel):
  """Section B: Code-Based Modeling specific inputs."""

  section_b = models.ForeignKey(SectionB, on_delete=models.CASCADE)


class SoftwareApplicationDevelopment(EpaBaseModel):
  """Section B: Software and Application Development specific inputs."""

  section_b = models.ForeignKey(SectionB, on_delete=models.CASCADE)


class SocialSciences(EpaBaseModel):
  """Section B: Social Sciences specific inputs."""

  section_b = models.ForeignKey(SectionB, on_delete=models.CASCADE)
