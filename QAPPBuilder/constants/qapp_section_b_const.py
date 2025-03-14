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

# Programmatic solution to get max len?
DISCIPLINE_MAX_LEN = max(len(choice[0]) for choice in DISCIPLINE_CHOICES)

SECTION_B = {
    'b': {'header': 'B: Implementing Environmental Information Operations'},
    'b1': {
        'header': 'B1: Identification of Project Environmental Information'
        'Operations'
    },
    'b2': {'header': 'B2: Methods for Environmental Information Acquisition'},
    'b3': {'header': 'B3: Integrity of Environmental Information'},
    'b4': {'header': 'B4: Quality Control'},
    'b5': {
        'header': 'B5: Instruments/Equipment Calibration, Testing, '
        'Inspection, and Maintenance'
    },
    'b6': {'header': 'B6: Inspection/Acceptance of Supplies and Services'},
    'b7': {'header': 'B7: Environmental Information Management'},
    'b71': {'header': 'B7.1: Information Handling and Storage'},
    'b72': {'header': 'B7.2: Information Security'},
    'b73': {
        'header': 'B7.3: Information Systems',
        'boilerplate': 'Table 6 below identifies the types of hardware, '
        'operating systems (OS), and specialty software that will be used for '
        'this project, including any specialized requirements requiring the '
        'use of anything other than the standard EPA-issued laptop with '
        'Microsoft Windows OS using Microsoft Office Tools.'
    },
    'b74': {
        'header': 'B7.4: Information Accessibility',
        'boilerplate': 'Data that belong to the Federal government are '
        'subject to the Federal Information Security Modernization Act '
        '(FISMA). Research data associated with any scientific product, as '
        'appropriate, will be shared publicly after clearance and acceptance '
        'of the product by a journal, either through Science Hub or another '
        'data repository. The metadata of the publicly available data will be '
        'recorded in Science Hub which transmits this information to data.gov.'
    }
}
