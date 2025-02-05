QAPP_TYPES = ['Standard', 'Discipline Specific']

SECTION_A_INDEX = 0
SECTION_B_INDEX = 1
SECTION_C_INDEX = 2
SECTION_D_INDEX = 3

QAPP_SECTIONS = ['A', 'B', 'C', 'D']

QAPP_DESCRIPTIONS = [
  'Project Management and Information/Data Quality Objectives',
  'Implementing Environmental Information Operations',
  'Assessments and Response Actions and Oversight',
  'Environmental Information Review and Usability Determination'
]

DISCIPLINES = {
  'CBM': 'Code-Based Modeling',
  'ET': 'Environmental Technology',
  'ED': 'Existing Data',
  'MM': 'Measurement and Monitoring',
  'MAE': 'Model Application and Evaluation',
  'SS': 'Social Science',
  'SAD': 'Software and Application Development'
}

STANDARD_SECTIONS = [
  {
    'key': QAPP_SECTIONS[SECTION_A_INDEX],
    'desc': QAPP_DESCRIPTIONS[SECTION_A_INDEX],
    'subsections': [
      {
        ''
      }
    ]
  }
]

SECTION_A_1_HELP = {
  'title': '''Provide the name/title of the document to include
              'Quality Assurance Project Plan'.''',
  'version_date': '''Provide the date the draft QAPP was prepared for
                     signature (Version Date).''',
  'conducting_org_name': '''Provide the name of the organization conducting the
                            environmental information operations.''',
  'developing_org_name': '''
    Provide the name of organization that developed the QAPP
    (if different from organization conducting the work).''',
  'applicability_period': 'Specify the period of applicability.',
  'versions': 'Allow many to many for version control info.',
  'doc_control_identifier': '''Provide the document\'s document control
                               identifier (i.e., ORD QA Track ID).''',
  'agreement_num': '''Grant or cooperative agreement number if the work is
                      being performed under an EPA assistance agreement.''',
  'con_to_num': '''Contract number and Task Order (TO) number if the work is
                   being performed under an acquisition.''',
  'ia_num': '''
    Interagency agreement number if the work is being performed under an
    interagency agreement (IA).''',
  'mou_title': 'Title and date of Memorandum of Understanding (MOU)/Agreement.',
  'mou_date': 'Date of Memorandum of Understanding (MOU)/Agreement.',
  'reg_req_cit': 'Citation of the regulatory requirement, if applicable.',
  'enf_legal_title': '''Title and date of the enforcement or legal agreement,
                        if applicable.''',
  'enf_legal_date': '''Date of the enforcement or legal agreement,
                       if applicable.''',
  'ord_qa_cat': '''
    Identify the project\'s ORD QA Category designation (see ORD PPM 13.07:
    Use of the Graded Approach for Quality Assurance of Research).''',
  'ord_program': '''Identify the ORD national program or activity that the
                    research supports (if required by your center).''',
  'definitions': '''Define any abbreviations/acronyms in the title or
                    name of the QAPP.''',
}

SECTION_A_2_HELP = {
  'epa_op_man': '''Signature of EPA Operations Manager
                   (i.e., ORD Technical Lead (TL) or designee).''',
  'epa_qam': '''Signature of EPA QAM, or designee as specified in
                the organization\'s QMP.''',
  'non_epa_op_man': '''Signature of the non-EPA Operations Manager
                       (Extramural Technical Manager) or designee.''',
  'non_epa_qam': '''
    Signature of the non-EPA Project QAM or an individual from the non-EPA
    organization with QA responsibilities for the project.''',
  'supervisor': '''Signature from direct line supervisor of the
                   EPA Operations Manager or designee.''',
  'pqapp_dir': '''
    For programmatic QAPPs (PQAPPs), signature of Center/Office Director of
    QA (recommended for QA Category B, required for QA Category A).'''
}
