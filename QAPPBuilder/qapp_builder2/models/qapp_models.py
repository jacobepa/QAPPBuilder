from django.contrib.auth.models import User
from django.db import models
from qapp_builder2.models.section_a_models import SectionA
from teams.models import Team


class Qapp(models.Model):

  created_by = models.ForeignKey(User)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  teams = models.ManyToManyField(Team, through='QappSharingTeamMap')
  section_a = models.ForeignKey(SectionA)
