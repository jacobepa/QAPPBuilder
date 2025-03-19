from qapp_builder.models import Qapp, SectionA1, SectionA2, SectionA4, \
    SectionA5, SectionA6, SectionA10, SectionA11, SectionB, SectionB7, \
    SectionC, SectionD
from qapp_builder.models.utility_models import EpaBaseModel


QAPP_PAGE_INDEX = {
    'qapp': 0,
    'section-a1': 1,
    'section-a2': 2,
    'section-a3': 3,
    'section-a4': 4,
    'section-a5': 5,
    'section-a6': 6,
    'section-a7': 7,
    'section-a8': 8,
    'section-a9': 9,
    'section-a10': 10,
    'section-a11': 11,
    'section-a12': 12,
    'section-b': 13,
    'section-b7': 14,
    'section-c': 15,
    'section-d': 16
}


def get_progress(qapp_id, model_class: EpaBaseModel):
    obj = model_class.objects.filter(qapp_id=qapp_id).first()
    if not obj:
        return 0
    return obj.get_progress()


def get_qapp_page_list(qapp_id):
    qapp = Qapp.objects.get(id=qapp_id)
    return [
        {'tail_path': '/detail/', 'label': 'QAPP Details',
         'progress': qapp.get_progress()},
        {'tail_path': '/section-a1/detail/', 'label': 'Section A1',
         'progress': qapp.get_progress('section_a1')},
        {'tail_path': '/section-a2/detail/', 'label': 'Section A2',
         'progress': qapp.get_progress('section_a2')},
        {'tail_path': '/section-a3/', 'label': 'Section A3', 'progress': 100},
        {'tail_path': '/section-a4/detail/', 'label': 'Section A4',
         'progress': qapp.get_progress('section_a4')},
        {'tail_path': '/section-a5/detail/', 'label': 'Section A5',
         'progress': qapp.get_progress('section_a5')},
        {'tail_path': '/section-a6/detail/', 'label': 'Section A6',
         'progress': qapp.get_progress('section_a6')},
        {'tail_path': '/section-a7/', 'label': 'Section A7', 'progress': 100},
        {'tail_path': '/section-a8/', 'label': 'Section A8', 'progress': 100},
        {'tail_path': '/section-a9/', 'label': 'Section A9', 'progress': 100},
        {'tail_path': '/section-a10/detail/', 'label': 'Section A10',
         'progress': qapp.get_progress('section_a10')},
        {'tail_path': '/section-a11/detail/', 'label': 'Section A11',
         'progress': qapp.get_progress('section_a11')},
        {'tail_path': '/section-a12/', 'label': 'Section A12', 'progress': 100},
        {'tail_path': '/section-b/detail/', 'label': 'Section B',
         'progress': qapp.get_progress('section_b')},
        {'tail_path': '/section-b7/detail/', 'label': 'Section B7',
         'progress': qapp.get_progress('section_b7')},
        {'tail_path': '/section-c/detail/', 'label': 'Section C',
         'progress': qapp.get_progress('section_c')},
        {'tail_path': '/section-d/detail/', 'label': 'Section D',
         'progress': qapp.get_progress('section_d')},
    ]
