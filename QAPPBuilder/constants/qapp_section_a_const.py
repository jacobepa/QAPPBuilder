QAPP_TITLE_HEADER = 'U.S. Environmental Protection Agency ' + \
    'Office of Research and Development'

PROJ_ROLES_RESPONSIBILITIES = {
    'QA Manager': [
        'Provides QA training/review on the ORD QA Program.',
        '''Assists the ORD TL in ensuring that quality requirements are
           identified for the project.''',
        'Reviews and approves QAPP.',
        '''Reviews and approves ORD sub-products and products developed under
           the project QAPP.''',
        '''Reports quality related issues to the TL's supervisor and
           organization's senior manager.'''
    ],
    'Branch Chief': [
        'Consults with TL and QAM on QA category designation.',
        'Reviews and approves QAPP.',
        '''Communicates regularly with project TL to ensure that QA requirements
           are met.''',
        '''Evaluates and seeks to provide the necessary resources to accomplish
           the work described in the QAPP.''',
        'Ensures that no EIO begins until the QA documentation is approved.'
    ],
    'Division Director': [
        '''Provides the necessary resources (personnel, funding, materials,
           supplies, and time) to accomplish the work described in the project
           QAPP.''',
        '''Ensures the roles and responsibilities of division personnel meet
           project specific and organizational specific requirements as
           specified in QAPPs and the ORD QMP'''
    ],
    'Technical Lead': [
        '''Maintains and distributes the official, approved copy of this QAPP
           to project EIO participants.''',
        '''Reviews project QAPP annually for consistency with the current EIO
           of the project and updates the QAPP to match the current EIO of
           the project as necessary.''',
        '''Notifies their QAM in writing of any quality related issue or
           deviation from QA documentation.''',
    ],
}

SECTION_A = {
    'a1': {
        'header': 'A1: Title Page',
        'labels': {
            'qapp': 'QAPP',
            'ord_center': 'ORD Center',
            'division': 'Division',
            'branch': 'Branch',
            'title': 'Title',
            'ord_national_program': 'ORD National Program',
            'version_date': 'Version Date',
            'proj_qapp_id': 'Project QAPP ID (QA Track ID)',
            'qa_category': 'QA Category',
            'intra_or_extra': 'QAPP Developed Intra-or-Extramurally',
            'vehicle_num': 'Vehicle #',
            'non_epa_org': 'Name of Non-EPA Organization',
            'period_performance': 'Perior of Performance (POP)',
            'accessibility': 'QAPP Accessibility'
        }
    },
    'a2': {
        'header': 'A2: Approval Page',
        'labels': {
            'ord_technical_lead': 'ORD Technical Lead (TL)',
            'ord_tl_supervisor': 'ORD Technical Lead\'s Supervisor',
            'ord_qa_manager': 'ORD QA Manager',
            'extramural_technical_manager': 'Extramural Technical Manager',
            'extramural_qa_manager': 'Extramural QA Manager'
        }
    },
    'a3': {
        'header': 'A3: Table of Contents, Document Format, and Document Control'
    },
    'a4': {
        'header': 'A4: Project Purpose, Problem Definition, and Background',
        'boilerplate': '''
            Environmental information operations (EIO) conducted under this
            Quality Assurance Project Plan (QAPP) will adhere to the
            requirements specified in the Office of Research and Development
            (ORD) Quality Management Plan (QMP).
        '''
    },
    'a4_1': {
        'header': 'A4.1: Project Background'
    },
    'a4_2': {
        'header': 'A4.2: Project Purpose and Problem Definition'
    },
    'a5': {
        'header': 'Project Task Description',
        'boilerplate': '''
            The Table below lists expected tasks and products for this project
            in relation to their anticipated start and projected end dates by
            Fiscal Year (FY).
        '''
    },
    'a6': {
        'header': '''Information/Data Quality Objectives and
                     Performance/Acceptance Criteria'''
    },
    'a7': {
        'header': 'Distribution List',
        'boilerplate': '''
            The EPA Technical Lead (TL) is responsible for maintaining a copy
            of the original approved QAPP and all approved subsequent revisions
            of the QAPP within their project file. The Technical Lead (TL) is
            responsible for the distribution of the most current signed approved
            version of the QAPP to participants as indicated in Table 2 below.
        '''
    },
    'a8': {
        'header': 'A8: Project Organization',
        'boilerplate': '''
            The roles and responsibilities of individuals involved in performing
            research activities and developing products within this project are
            identified in the below Table.
        '''
    },
    'a9': {
        'header': 'A9: Project Quality Assurance Manager Independence',
        'boilerplate': '''
            ORD QA Managers are independent from all EIO for any project for
            which they serve as Project QA Manager for, as indicated in the ORD
            QMP and Table 3 within Section A8 of this QAPP. Figure 1 in
            Section A10, shows the independence of ORD Project QA Manager from
            the project participants and EIO within this project.
        '''
    },
    'a10': {
        'header': 'A10: Project Organization Chart and Communications',
        'boilerplate': '''
            Figure 1 organization chart provides a visual representation of the
            working relationships and lines of communication among all project
            participants identified in Table 3. Any issues identified by an
            individual within the project will notify the TL. The TL will notify
            their QA Manager in writing of any quality related issue or
            deviation from QA Documentation. The QA Manager has the authority to
            access and discuss quality related issues with their organization's
            senior manager.
        '''
    },
    'a11': {
        'header': 'A11: Personnel Training/Certification'
    },
    'a12': {
        'header': 'A12: Documents and Records',
        'boilerplate': '''
            Research activities must be documented according to the requirements
            of ORD QA Policies titled Scientific Recordkeeping: Paper,
            Scientific Recordkeeping: Electronic, and Quality Assurance/Quality
            Control Practices for ORD Laboratory and Field-Based Research, as
            well as requirements defined in this QA Project Plan.

            The ORD QA Policies require the use of research notebooks and
            the management of research records, both paper and electronic, such
            that project research data generation may continue even if a
            researcher or an analyst participating in the project leaves the
            project staff.

            Detailed information regarding project file location and managing of
            data can be found in section B7.

            Table 4 provides a list of documents and records that will be
            generated for this project, the parties responsible for generating
            and updating those records, storage locations, and file types. The
            ORD technical lead will be responsible for maintaining a copy of all
            file records in accordance with the EPA records schedule identified
            in Table 5.
        '''
    }
}
