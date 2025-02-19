from os.path import join, dirname, realpath

DISCIPLINE_MM_STR = 'Measurement and Monitoring'
DISCIPLINE_SS_STR = 'Social Sciences'
DISCIPLINE_ED_STR = 'Existing Data'
DISCIPLINE_CBM_STR = 'Code-Based Modeling'
DISCIPLINE_MAE_STR = 'Model Application and Evaluation'
DISCIPLINE_SAD_STR = 'Software and Application Development'
DISCIPLINE_ET_STR = 'Environmental Technology'

DISCIPLINE_CHOICES = (
  (DISCIPLINE_MM_STR, DISCIPLINE_MM_STR),
  (DISCIPLINE_SS_STR, DISCIPLINE_SS_STR),
  (DISCIPLINE_ED_STR, DISCIPLINE_ED_STR),
  (DISCIPLINE_CBM_STR, DISCIPLINE_CBM_STR),
  (DISCIPLINE_MAE_STR, DISCIPLINE_MAE_STR),
  (DISCIPLINE_SAD_STR, DISCIPLINE_SAD_STR),
  (DISCIPLINE_ET_STR, DISCIPLINE_ET_STR),
)

dir_path = dirname(realpath(__file__))
MODEL_LABELS_JSON_DIR = join(dir_path, './section_b_model_labels')
MODEL_LABELS_JSON_PATHS = {}
for choice, _ in DISCIPLINE_CHOICES:
  MODEL_LABELS_JSON_PATHS[choice] = join(
    MODEL_LABELS_JSON_DIR, choice.replace(' ', '-') + '.json')

SECTION_B_BASE_LABELS = {
  # B1: Identification of Project Environmental Information Operations
  'eio_detail': 'Describe in detail the EIO to be conducted for the project.',
  'proj_purpose': 'Describe in detail how the project purpose (from Section A4)'
                  'will be satisfied based on the described EIO.',
  'perf_criteria': 'Describe in detail how the DQOs and performance and '
                   'acceptance criteria (from Section A6) will be satisfied '
                   'based on the described EIO.',
  # ---------------------------------------------------------------------------
  # B2: Methods for Environmental Information Acquisition
  'methods_procedures': 'Identify and describe the methods and procedures for '
                        'how environmental information will be acquired '
                        'throughout the project including any implementation '
                        'requirements. The acquisition of environmental '
                        'information includes collection, production, '
                        'evaluation and/or use as well as design, construction'
                        ', operation, or application of environmental '
                        'technology.',
  'methods_specifics': 'Identify methods (e.g., EPA Standard Method, NIST, '
                       'ISO, ASTM, etc.) utilized by listing the following:',
  'sops_env_info_acquisition': 'Identify and describe any SOPs used for the '
                               'acquisition of environmental information '
                               'including the:',
  # TODO: Table B-1. Example SOP Details for this Project
  # TODO: Table B-2. Example Field Sampling Table
  # ---------------------------------------------------------------------------
  # B3: Integrity of Environmental Information
  'integrity_procedures': 'Describe or cite the procedures for ensuring the '
                          'integrity of the EIO.',
  # ---------------------------------------------------------------------------
  # B4: Quality Control
  'qc_activities': 'Identify and describe the Quality Control (QC) activities '
                   'needed for each environmental information operation to '
                   'meet project environmental information/data quality '
                   'objectives and performance/acceptance criteria.',
  'qc_frequency': 'Describe or cite the frequency of each type of QC activity, '
                  'corrective actions, and how the effectiveness of the '
                  'corrective action shall be determined and documented.',
  'statistics_procedures': 'Describe or reference the procedures to be used to '
                           'calculate applicable statistics '
                           '(e.g., precision and bias).',
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
  'services_personnel': 'Identify the individual(s) responsible for inspection '
                        'and acceptance of services.',
  'services_provided': 'Identify the services provided by vendors to be '
                       'inspected and accepted to include, but not limited to '
                       'contractors, sub-contractors, and sub-grantees which '
                       'may include: document development, and performing EIO.',
  'services_procedures': 'Describe or reference the procedures for how '
                         'services will be inspected and accepted.',
  'services_doc': 'Identify how the acceptance of services will be documented, '
                  'either on deliverables themselves or through documented '
                  'information traceable to the deliverable.',
  'vendor_qapp_elements': 'Specify the elements of the QAPP Standard for which '
                          'the vendor is responsible for.',
  'vendor_qapp_adherence': 'Identify how the vendor\'s adherence to the '
                           'QAPP requirements will be verified.',
  # ---------------------------------------------------------------------------
  # B7: Environmental Information Management
  # --- B7.1: Information Handling and Storage
  # NOTE: env_info_management_proc has 4 sub-bullets
  'env_info_management_proc': 'Describe or cite the environmental information '
                              'management process for the project, tracing the '
                              'path of the environmental information from its '
                              'generation to its final use or storage (e.g., '
                              'the field, the laboratory, the office, the '
                              'database), including:',
  # NOTE: doc_procedures has 4 sub-bullets
  'doc_procedures': 'Describe or reference standard documentation procedures '
                    'for working data/information files, including:',
  'info_processing_procedures': 'Describe or reference all procedures to '
                                'process, compile, and analyze the information.'
                                ' This includes procedures for addressing '
                                'environmental information generated as part '
                                'of the project as well as environmental '
                                'information from other sources.',
  # --- B7.2: Information Security
  # data_control': '',
  # NOTE: data_control has one primary field with four sub-bullets...
  'data_transference': 'Describe procedures for how data will be transferred '
                       'from the source of generation or collection to the '
                       'project file such as retrieving raw data from '
                       'analytical instruments, nonnetworked computers, '
                       'transcribing of manually generated data to '
                       'spreadsheet, etc., as applicable.',
  'perm_retention_conversion': 'For QA Category A projects (permanent '
                               'retention): Describe how the environmental '
                               'information will be converted, if necessary, '
                               'and retained, in a non-proprietary, universal/'
                               'standard file format, if possible, by the end '
                               'of the project for acceptability by National '
                               'Archives and Records Administration (NARA). '
                               'NOTE: Any information recorded related to a '
                               'project in logbooks such as a shared '
                               'calibration logbook, must be preserved and '
                               'kept with the project file. This may result in '
                               'scanning physical shared logbooks and the '
                               'process for preservation needs to be discussed '
                               'for Category A research.',
  'data_special_agreements': 'Identify any special agreements (e.g., data use '
                             'agreements) and describe data security measures '
                             'for protecting scientific data consistent with '
                             'applicable laws, regulations, rules, and '
                             'policies including scientific data deemed '
                             'necessary to restrict or limit access, protect '
                             'CUI, intellectual property, as applicable.',
  'data_forms_checklists': 'Provide or reference examples of any forms or '
                           'checklists to be used in these processes.',
  # --- B7.3: Information Systems
  # Document hardware, software, and performance requirements:
  'specialized_hardware': 'Identify specialized hardware necessary for the '
                          'project beyond standard issued EPA equipment (e.g., '
                          'high-performance computing systems, etc.)',
  'specialized_software': 'Identify any specialized software (including version'
                          ') and/or operating systems beyond standard pre-'
                          'installed EPA software (e.g., Microsoft Office '
                          'applications, etc.) used in the generation, '
                          'processing, or reporting of environmental '
                          'information.',
  'config_procedures': 'Describe or reference the procedures to demonstrate '
                       'acceptability of the hardware/software configuration '
                       'required for assuring that applicable information '
                       'resource management requirements are satisfied.'
                       'Describe any specifications needed for processing '
                       'power to accommodate complex statistical analysis or '
                       'modeling activities. If no special requirements are '
                       'needed then include the following statement: "There '
                       'are no special hardware, software, and performance '
                       'requirements anticipated for this project."',
  # TODO: Table 6. Req Hardware, OS, and Types of Specialized Software for EIO
  # --- B7.4: Information Accessibility
  'public_data_preservation': 'Describe the plan for the long-term '
                              'preservation of publicly accessible research '
                              'data, as appropriate.',
}

# B5: Instruments/Equipment Calibration, Testing, Inspection, and Maintenance
# Field, Laboratory and/or Environmental Technology Activities ONLY
# TODO: These fields aren't present in the Discipline Specific template.
#       Does that mean that everything discipline-specific in the standard
#       template needs to be copied into the discipline specific template also?
EQUIPMENT_SECTION_LABELS = {
  'equipment_used': 'Identify all instruments/equipment used for EIO, '
                    'including, but not limited to: tools, gauges, and pumps.',
  'equipment_procedures_docs': 'Describe all procedures and documentation '
                               'activities that will be performed to ensure'
                               'that the instruments/equipment are available '
                               'and in working order when needed.',
  'equipment_calibration': 'Describe or reference how calibration will be '
                           'conducted, documented, and traceable to the '
                           'instrument.',
  'equipment_testing_maint': 'Describe or reference procedures and '
                             'documentation activities for instrument and '
                             'equipment testing, inspection, and maintenance.',
  'spare_parts': 'Describe the availability of critical spare parts, '
                 'identified in the operating guidance and/or design '
                 'specifications of the instruments/equipment.'
}

"""
Labels for model FieldLabSection which are shared with both
FieldActivity and LaboratoryActivity models.
"""
FIELD_LAB_LABELS = {
  # B4.Field/LabActivities
  'field_lab_qc_desc': 'Describe the use of the following QC activities, as '
                       'applicable: blanks, duplicates, matrix spikes, '
                       'laboratory control samples, and surrogates.',
  # B6: Inspection/Acceptance of Supplies and Services
  # Lab and Field Supplies
  'supply_personnel': 'Identify the individual(s) responsible for inspection '
                      'and acceptance of supplies.',
  'supplies_to_inspect': 'Identify the supplies provided by vendors to be '
                         'inspected and accepted to include, but limited to: '
                         'spare parts for instruments/equipment, standard '
                         'materials and solutions, sample bottles, calibration '
                         'gases, reagents, hoses, deionized water, potable '
                         'water, and electronic data storage media.',
  'inspection_procedures': 'Describe or reference the procedures for how '
                           'supplies will be inspected and accepted.',
  'acceptance_doc': 'Identify how the acceptance of supplies will be '
                    'documented, either items themselves or in documented '
                    'information traceable to the items.',
  **EQUIPMENT_SECTION_LABELS
}

"""Labels for model FieldActivity."""
FIELD_ACTIVITY_LABELS = {
  # B2.FieldActivities
  'field_procedures': 'Describe or reference detailed descriptions of '
                      'procedures for all field activities including but not '
                      'limited to information derived from: tools, '
                      'instruments, observational results, investigations, and '
                      'sample collection.',
  'field_description': 'Describe: sample extraction and/or analysis (reference '
                       'maximum holding times), selection and preparation of '
                       'sample containers, sample volumes, preservation '
                       'methods, and sample handling and custody.',
  # B3.FieldActivities
  'field_sample_custody': 'Describe or cite procedures and requirements for '
                          'sample handling and custody to include but not '
                          'limited to: field logs, packaging, transport and/or '
                          'shipment from the site, and storage at the '
                          'laboratory.',
  'field_labels_and_logs': 'QAPP shall contain examples of the following: '
                           'sample labels, and chain of custody forms/sample '
                           'custody logs.',
  **FIELD_LAB_LABELS
}


"""Labels for model LaboratoryActivity"""
LABORATORY_ACTIVITY_LABELS = {
  # B2.LaboratoryActivities
  'lab_analytical_methods': 'Identify all analytical methods utilized via the '
                            'following: number/identifier (e.g., ORD QA Track '
                            'ID), version/revision date, and regulatory '
                            'citation (if applicable).',
  'lab_sops': 'Describe or reference SOPs that address procedures to be '
              'conducted when a noncompliance or failure in the analytical '
              'system occurs, who is responsible for corrective action, and '
              'how to determine and document the effectiveness of the '
              'corrective action.',
  'lab_turnaround_time': 'Specify the laboratory data package turnaround time '
                         'needed, if important to the project schedule. NOTE: '
                         'It is recommended to identify what is in the data '
                         'package in this section.',
  'lab_method_information': 'For non-standard method applications, such as for '
                            'unusual sample matrices and situations, describe '
                            'the appropriate method performance study '
                            'information needed to confirm the performance of '
                            'the method for the matrix. If previous '
                            'performance studies are not available, the QAPP '
                            'shall describe how performance studies will be '
                            'developed during the project and included as part '
                            'of the project results.',
  # B3.LabActivities
  'lab_laboratories_list': 'Identify each laboratory to be used as well as a '
                           'backup laboratory if identified as required in '
                           'systematic planning, contract statements of work, '
                           'or workplans.',
  'lab_laboratories_accred': 'Describe the processes for ensuring the '
                             'laboratory maintains current accreditation '
                             'and/or certification for applicable analytes '
                             'and matrices.',
  **FIELD_LAB_LABELS
}
