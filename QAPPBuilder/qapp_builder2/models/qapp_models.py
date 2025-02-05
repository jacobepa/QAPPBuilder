from django.db import models
from qapp_builder2.models.section_a_models import SectionA
from teams.models import Team


class Qapp(models.Model):

  teams = models.ManyToManyField(Team, through='QappSharingTeamMap')
  section_a = models.ForeignKey(SectionA)
