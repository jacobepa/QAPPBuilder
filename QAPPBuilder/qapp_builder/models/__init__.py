from django.apps import apps
from .utility_models import QappDocument
from .qapp_models import Qapp, QappSharingTeamMap, AcronymAbbreviation, Revision
from .section_a_models import (
    SectionA1, SectionA2, SectionA4, SectionA5, SectionA6,
    SectionA11, Discipline, AdditionalSignature,
    Distribution, RoleResponsibility, SectionA10, DocumentRecord
)
from .section_b_c_d_models import SectionB, SectionB7, \
    SectionC, SectionD, HardwareSoftware
