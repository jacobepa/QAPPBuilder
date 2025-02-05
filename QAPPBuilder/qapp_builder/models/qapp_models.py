from django.contrib.auth.models import User
from django.db import models
from .section_a_models import SectionA
from teams.models import Team


class Qapp(models.Model):

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  teams = models.ManyToManyField(Team)  # , through='QappSharingTeamMap2')
  section_a = models.ForeignKey(SectionA, on_delete=models.CASCADE)
  # TODO other sections


# class QappSharingTeamMap2(models.Model):
#   """Mapping between QAPP and Teams they share."""

#   added_date = models.DateTimeField(
#     auto_now_add=True, blank=False, editable=False)
#   qapp = models.ForeignKey(
#     Qapp, blank=False, related_name='qapp_teams2',
#     on_delete=models.CASCADE)
#   team = models.ForeignKey(Team, blank=False,
#                            related_name='team_qapp2',
#                            on_delete=models.CASCADE)
#   # Indicates if the team can edit the project.
#   can_edit = models.BooleanField(blank=False, default=True)
