from django.db import models
from .qapp_models import Qapp
from .utility_models import EpaBaseModel
from constants.utils import get_attachment_storage_path
from constants.qapp_section_a_const import SECTION_A, INTRA_EXTRA_CHOICES, \
    QA_CATEGORY_OPTIONS, ORD_CENTER_OPTIONS
from constants.qapp_section_b_const import DISCIPLINE_CHOICES, \
    DISCIPLINE_MAX_LEN


class Discipline(EpaBaseModel):

    name = models.CharField(
        blank=False, null=False, max_length=DISCIPLINE_MAX_LEN,
        choices=DISCIPLINE_CHOICES)

    def __str__(self):
        return self.name


class SectionA1(EpaBaseModel):

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, related_name='section_a1')
    ord_center = models.CharField(blank=False, null=False, max_length=55,
                                  choices=ORD_CENTER_OPTIONS)
    # TODO: Choices for Division?
    division = models.TextField(blank=False, null=False)
    # TODO: Choices for Branch?
    branch = models.TextField(blank=False, null=False)
    # NOTE: While title is under Section A1 in the actual QAPPs themselves,
    # it makes more sense to put it under the QAPP model.
    # title = models.TextField(blank=False, null=False)
    # TODO: Choices for National Program?
    ord_national_program = models.TextField(blank=False, null=False)
    version_date = models.DateField(blank=False, null=False)
    proj_qapp_id = models.TextField(blank=False, null=False)
    qa_category = models.CharField(
        blank=False, null=False, max_length=1, choices=QA_CATEGORY_OPTIONS)
    # Intramurally or Extramurally
    intra_or_extra = models.CharField(
        blank=False, null=False, max_length=12, choices=INTRA_EXTRA_CHOICES)
    # If extramurally:
    vehicle_num = models.TextField(blank=True, null=True)
    non_epa_org = models.TextField(blank=True, null=True)
    period_performance = models.TextField(blank=True, null=True)
    # Accessibility is "I do NOT want this QAPP internally shared and
    #                   accessible on the ORD intranet site."
    accessibility = models.BooleanField(default=False)
    disciplines = models.ManyToManyField(Discipline)
    # TODO: Measurement and Monitoring splits in two sub-options:
    #       Analytical Methods Development
    #       Animal/Cell Culture Studies
    # TODO: The CESER template has an "Other" option with user defined name...

    @property
    def labels(self):
        return SECTION_A['a1']['labels']


class SectionA2(EpaBaseModel):

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, related_name='section_a2')
    # Required Signatures:
    ord_technical_lead = models.TextField(blank=False, null=False)
    ord_tl_supervisor = models.TextField(blank=False, null=False)
    ord_qa_manager = models.TextField(blank=False, null=False)
    # Extramural signatures:
    extramural_technical_manager = models.TextField(blank=True, null=True)
    extramural_qa_manager = models.TextField(blank=True, null=True)
    # Optional additional signatures table

    @property
    def labels(self):
        return SECTION_A['a2']['labels']


class AdditionalSignature(EpaBaseModel):

    section_a2 = models.ForeignKey(SectionA2, on_delete=models.CASCADE)
    title = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)


class SectionA4(EpaBaseModel):

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, related_name='section_a4')
    project_background = models.TextField(blank=False, null=False)
    project_purpose = models.TextField(blank=False, null=False)

    @property
    def labels(self):
        return SECTION_A['a4']['labels']


class SectionA5(EpaBaseModel):

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, related_name='section_a5')
    tasks_summary = models.TextField(blank=False, null=False)
    # Table 1. Project Completion Timeline
    start_fy = models.CharField(blank=True, null=True, max_length=4)
    start_q = models.CharField(blank=True, null=True, max_length=2)

    @property
    def labels(self):
        return SECTION_A['a5']['labels']


class Task(EpaBaseModel):

    section_a5 = models.ForeignKey(SectionA5, on_delete=models.CASCADE)
    tasks_desc = models.TextField(blank=False, null=False)
    fy_q_0 = models.TextField(blank=True, null=True)
    fy_q_1 = models.TextField(blank=True, null=True)
    fy_q_2 = models.TextField(blank=True, null=True)
    fy_q_3 = models.TextField(blank=True, null=True)
    fy_q_4 = models.TextField(blank=True, null=True)
    fy_q_5 = models.TextField(blank=True, null=True)
    fy_q_6 = models.TextField(blank=True, null=True)
    fy_q_7 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.tasks_desc


class SectionA6(EpaBaseModel):

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, related_name='section_a6')
    information = models.TextField(blank=False, null=False)

    @property
    def labels(self):
        return SECTION_A['a6']['labels']


class Distribution(EpaBaseModel):

    qapp = models.ForeignKey(Qapp, on_delete=models.CASCADE)
    name = models.TextField(blank=False, null=False)
    org = models.TextField(blank=False, null=False)
    email = models.TextField(blank=False, null=False)
    proj_role = models.TextField(blank=False, null=False)

    @property
    def labels(self):
        return {
            'name': 'Name',
            'org': 'Organization',
            'email': 'Contact Information (e-mail)',
            'proj_role': 'Project Role(s)'
        }


# SectionA7 has no input except tables

# SectionA8 has no input except tables


class RoleResponsibility(EpaBaseModel):

    qapp = models.ForeignKey(Qapp, on_delete=models.CASCADE)
    name = models.TextField(blank=False, null=False)
    org = models.TextField(blank=False, null=False)
    proj_role = models.TextField(blank=False, null=False)
    proj_responsibilities = models.TextField(blank=False, null=False)

    @property
    def labels(self):
        return {
            'name': 'Name',
            'org': 'Organization',
            'proj_role': 'Project Role(s)',
            'proj_responsibilities': 'Project Responsibilities'
        }


# SectionA9 is static content, no input.

# SectionA10 is an optional(?) org chart
class SectionA10(EpaBaseModel):

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, related_name='section_a10')
    org_chart = models.FileField(null=True, blank=True,
                                 upload_to=get_attachment_storage_path)


class SectionA11(EpaBaseModel):

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, related_name='section_a11')
    information = models.TextField(blank=False, null=False)

    @property
    def labels(self):
        return SECTION_A['a11']['labels']


# SectionA12 has no input except tables


class DocumentRecord(EpaBaseModel):

    qapp = models.ForeignKey(Qapp, on_delete=models.CASCADE)
    record_type = models.TextField(blank=False, null=False)
    responsible_party = models.TextField(blank=False, null=False)
    in_proj_file = models.TextField(blank=False, null=False)
    file_type = models.TextField(blank=False, null=False)
    special_handling = models.BooleanField(default=False)

    @property
    def labels(self):
        return {
            'record_type': 'Record Type',
            'responsible_party': 'Responsible Party',
            'in_proj_file': 'Located in Project File (Y/N), '
            'If No, Specify File Location',
            'file_type': 'File Type (Format)',
            'special_handling': 'Special Handling Required?'
        }


# TODO: How to do this? Might just be constant depending on QA Category
# class RecordSchedule(EpaBaseModel):

#     qapp = models.ForeignKey(Qapp, on_delete=models.CASCADE)
