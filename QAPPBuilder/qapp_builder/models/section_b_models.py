from django.db import models
from constants import qapp_section_b_const as con
from .qapp_models import Qapp
from .utility_models import EpaBaseModel


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

  class Meta:
    abstract = True


class FieldLabSection(EquipmentSection):
  """
  Abstract class containing fields that belong to both Field Activities
  and Laboratory Activities. This class will be inherited by those respective
  models.
  """

  # B4.Field/LabActivities
  field_lab_qc_desc = models.TextField()
  # B6: Inspection/Acceptance of Supplies and Services
  # Lab and Field Supplies
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
  env_info_management_proc = models.TextField()
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


# #############################################################################
# Start Discipline Specific Models ############################################
# #############################################################################


class MeasurementMonitoring(EpaBaseModel):
  """
  Section B: Measurement and Monitoring Discipline Specific inputs.

  2.A Measurement and Monitoring (Field/Lab) Requirements for Section 2
  of the ORD Discipline Specific QAPP Template
  """

  section_b = models.ForeignKey(SectionB, on_delete=models.CASCADE)
  # ###########################################################################
  # 2.A.1 Experimental Process
  # ----- All Measurement and Monitoring Activities
  exp_process_1 = models.TextField()
  exp_process_2 = models.TextField()
  exp_process_3 = models.TextField()
  # ----- Analytical Method Development
  analytical_method_1 = models.TextField()
  analytical_method_2 = models.TextField()
  analytical_method_3 = models.TextField()
  analytical_method_4 = models.TextField()
  # ----- Use of Animals
  animals_1 = models.TextField()
  animals_2 = models.TextField()
  animals_3 = models.TextField()
  # ----- Cell Culture
  cell_1 = models.TextField()
  cell_2 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.A.2 Sample Collection and Management
  samples_1 = models.TextField()
  samples_2 = models.TextField()
  samples_3 = models.TextField()
  samples_4 = models.TextField()
  samples_5 = models.TextField()
  samples_6 = models.TextField()
  samples_7 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.A.3 Experimental Procedures
  exp_procedure_1 = models.TextField()
  exp_procedure_2 = models.TextField()
  exp_procedure_3 = models.TextField()
  exp_procedure_4 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.A.4 Quality Control
  # ----- All Measurement and Monitoring Activities
  qc_mm_1 = models.TextField()
  qc_mm_2 = models.TextField()
  qc_mm_3 = models.TextField()
  qc_mm_4 = models.TextField()
  qc_mm_5 = models.TextField()
  qc_mm_6 = models.TextField()
  qc_mm_7 = models.TextField()
  # ----- Analytical Method Development
  qc_analyt_1 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.A.5 Data Review
  data_review_1 = models.TextField()
  data_review_2 = models.TextField()
  data_review_3 = models.TextField()
  data_review_4 = models.TextField()
  data_review_5 = models.TextField()
  data_review_6 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.A.6 Data Processing
  data_processing_1 = models.TextField()
  data_processing_2 = models.TextField()
  data_processing_3 = models.TextField()
  data_processing_4 = models.TextField()
  data_processing_5 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.A.7 Data Usability
  data_usability_1 = models.TextField()
  data_usability_2 = models.TextField()
  data_usability_3 = models.TextField()
  # ---------------------------------------------------------------------------


class SocialSciences(EpaBaseModel):
  """
  Section B: Social Sciences Discipline Specific inputs.

  2.B Social Sciences (SS) for Section 2 of the ORD Discipline Specific QAPP
  Template
  """
  section_b = models.ForeignKey(SectionB, on_delete=models.CASCADE)
  # ###########################################################################
  # 2.B.1 Social Study Design
  approach = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.B.2 Social Sciences Data Collection Methods
  data_collection_1 = models.TextField()
  data_collection_2 = models.TextField()
  data_collection_3 = models.TextField()
  data_collection_4 = models.TextField()
  data_collection_5 = models.TextField()
  data_collection_6 = models.TextField()
  data_collection_7 = models.TextField()
  data_collection_8 = models.TextField()
  data_collection_9 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.B.3 Social Sciences Data Integrity
  data_integrity_1 = models.TextField()
  data_integrity_2 = models.TextField()
  data_integrity_3 = models.TextField()
  data_integrity_4 = models.TextField()
  data_integrity_5 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.B.4 Social Sciences Data Analysis
  data_analysis_1 = models.TextField()
  data_analysis_2 = models.TextField()
  data_analysis_3 = models.TextField()
  data_analysis_4 = models.TextField()
  data_analysis_5 = models.TextField()
  # ---------------------------------------------------------------------------


class ExistingData(EpaBaseModel):
  """
  Section B: Existing Data Discipline Specific inputs.

  2.C Existing Data (ED) for Section 2 of the ORD Discipline Specific QAPP
  Template
  """

  section_b = models.ForeignKey(SectionB, on_delete=models.CASCADE)
  # ###########################################################################
  # 2.C.1 Methods of Environmental Information
  methods_ei_1 = models.TextField()
  methods_ei_2 = models.TextField()
  methods_ei_3 = models.TextField()
  methods_ei_4 = models.TextField()
  methods_ei_5 = models.TextField()
  methods_ei_6 = models.TextField()
  methods_ei_7 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.C.2 Environmental Information Quality Control
  ei_qc_1 = models.TextField()
  ei_qc_2 = models.TextField()
  ei_qc_3 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.C.3 Environmental Information Review
  ei_review_1 = models.TextField()
  ei_review_2 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.C.4 Useability Determination
  useability_constraints = models.TextField()
  # ---------------------------------------------------------------------------
  # TODO: Table B-4. Existing Data for Addressing Research
  #                  Questions & Data Limitations
  # ---------------------------------------------------------------------------


class CodeBasedModeling(EpaBaseModel):
  """
  Section B: Code-Based Modeling Discipline Specific inputs.

  2.D Code-Based Modeling (CBM) for Section 2 of the ORD Discipline Specific
  QAPP Template
  """

  section_b = models.ForeignKey(SectionB, on_delete=models.CASCADE)
  # ###########################################################################
  # 2.D.1 Requirements and Design
  reqs_design_1 = models.TextField()
  reqs_design_2 = models.TextField()
  reqs_design_3 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.D.2 Coding Processes
  # reqs_design_1 = models.TextField()
  reqs_design_1_1 = models.TextField()
  reqs_design_1_2 = models.TextField()
  reqs_design_1_3 = models.TextField()
  # reqs_design_2 = models.TextField()
  reqs_design_2_1 = models.TextField()
  reqs_design_2_2 = models.TextField()
  reqs_design_2_3 = models.TextField()
  reqs_design_2_4 = models.TextField()
  reqs_design_2_5 = models.TextField()
  # reqs_design_3 = models.TextField()
  reqs_design_3_1 = models.TextField()
  reqs_design_3_2 = models.TextField()
  reqs_design_3_3 = models.TextField()
  reqs_design_3_4 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.D.3 Tool Validation
  tool_validation_1 = models.TextField()
  tool_validation_2 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.D.4 Outputs and Results
  outputs_results_1 = models.TextField()
  outputs_results_2 = models.TextField()
  outputs_results_3 = models.TextField()
  outputs_results_4 = models.TextField()
  outputs_results_5 = models.TextField()
  # ---------------------------------------------------------------------------


class ModelApplicationEvaluation(EpaBaseModel):
  """
  Section B: Model Application and Evaluation Discipline Specific inputs.

  2.E Model Application and Evaluation (MAE) for Section 2 of the ORD Discipline
  Specific QAPP Template
  """

  section_b = models.ForeignKey(SectionB, on_delete=models.CASCADE)
  # ###########################################################################
  # 2.E.1 Model Specifications
  model_specs_1 = models.TextField()
  model_specs_2 = models.TextField()
  model_specs_3 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.E.2 Environmental Information Selection and Verification (Input Data)
  ei_sel_verification_1 = models.TextField()
  ei_sel_verification_2 = models.TextField()
  ei_sel_verification_3 = models.TextField()
  ei_sel_verification_4 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.E.3 Model Performance Assessment and Validation (Output Data)
  model_performance_1 = models.TextField()
  model_performance_2 = models.TextField()
  model_performance_3 = models.TextField()
  model_performance_4 = models.TextField()
  model_performance_5 = models.TextField()
  model_performance_6 = models.TextField()
  model_performance_7 = models.TextField()
  model_performance_8 = models.TextField()
  model_performance_9 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.E.4 Interpretation of Results
  results_interp_1 = models.TextField()
  results_interp_2 = models.TextField()
  # ---------------------------------------------------------------------------


class SoftwareApplicationDevelopment(EpaBaseModel):
  """
  Section B: Software and Application Development Discipline Specific inputs.

  2.F Software and Application Development (SAD) for Section 2 of the ORD
  Discipline Specific QAPP Template
  """

  section_b = models.ForeignKey(SectionB, on_delete=models.CASCADE)
  # ###########################################################################
  # 2.F.1 Application User Roles and Responsibilities
  roles_resp_1 = models.TextField()
  roles_resp_2 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.F.2 Requirements Collection
  requirements_1 = models.TextField()
  requirements_2 = models.TextField()
  requirements_3 = models.TextField()
  requirements_4_1 = models.TextField()
  requirements_4_2 = models.TextField()
  requirements_4_3 = models.TextField()
  requirements_4_4 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.F.3 System Design
  sys_design_1 = models.TextField()
  sys_design_2 = models.TextField()
  sys_design_3 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.F.4 Coding and Implementation
  coding_1 = models.TextField()
  coding_2 = models.TextField()
  coding_3 = models.TextField()
  coding_4 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.F.5 Verification and Validation
  vv_1 = models.TextField()
  vv_2 = models.TextField()
  vv_3 = models.TextField()
  vv_4_1 = models.TextField()
  vv_4_2 = models.TextField()
  vv_4_3 = models.TextField()
  # NOTE: There are also 3 subsections for vv_4_3, not sure if these should
  #       also be enumerated.
  vv_4_4 = models.TextField()
  vv_4_5 = models.TextField()
  vv_4_6 = models.TextField()
  vv_4_7 = models.TextField()
  vv_5 = models.TextField()
  # TODO: Table 12. Example of a Testing and Acceptance Criteria Table
  #       Used for Section 2.5 of Software and Application Development Project.
  # ---------------------------------------------------------------------------
  # 2.F.6 Maintenance and User Support
  support_1 = models.TextField()
  support_2 = models.TextField()
  support_3 = models.TextField()
  support_4 = models.TextField()
  support_5 = models.TextField()
  support_6_1 = models.TextField()
  support_6_2 = models.TextField()
  support_7 = models.TextField()
  support_7_1 = models.TextField()
  support_7_2 = models.TextField()
  # ---------------------------------------------------------------------------


class EnvironmentalTechnology(EquipmentSection):
  """
  Section B: Environmental Technology Discipline Specific inputs.

  2.G Environmental Technology (ET) for Section 2 of the ORD Discipline Specific
  QAPP Template
  """

  section_b = models.ForeignKey(SectionB, on_delete=models.CASCADE)
  # ###########################################################################
  # 2.G.1 System Elements
  system_1 = models.TextField()
  system_2 = models.TextField()
  system_3 = models.TextField()
  system_4 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.G.2 Process Elements and Quality Criteria
  process_1 = models.TextField()
  process_2 = models.TextField()
  process_3 = models.TextField()
  process_4 = models.TextField()
  process_5 = models.TextField()
  process_6 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.G.3 System Operation, Maintenance, and Training
  sysop_maint_train_1 = models.TextField()
  sysop_maint_train_2 = models.TextField()
  sysop_maint_train_3 = models.TextField()
  sysop_maint_train_4 = models.TextField()
  sysop_maint_train_5 = models.TextField()
  sysop_maint_train_6 = models.TextField()
  sysop_maint_train_7 = models.TextField()
  sysop_maint_train_8 = models.TextField()
  # ---------------------------------------------------------------------------
  # 2.G.4 Demobilization of Environmental Technology Projects
  demobilization = models.TextField()
  # ---------------------------------------------------------------------------
