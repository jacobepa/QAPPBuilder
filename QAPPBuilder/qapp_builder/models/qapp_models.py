from django.contrib.auth.models import User
from django.db import models
from teams.models import Team
from .utility_models import EpaBaseModel


class Qapp(EpaBaseModel):

    title = models.TextField(blank=False, null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    teams = models.ManyToManyField(Team, through='QappSharingTeamMap')

    def __str__(self):
        return self.title


class QappSharingTeamMap(EpaBaseModel):
    """Mapping between QAPP and Teams they share."""

    added_date = models.DateTimeField(
        auto_now_add=True, blank=False, editable=False)
    qapp = models.ForeignKey(
        Qapp, blank=False, related_name='qapp_teams2',
        on_delete=models.CASCADE)
    team = models.ForeignKey(Team, blank=False,
                             related_name='team_qapp2',
                             on_delete=models.CASCADE)
    # Indicates if the team can edit the project.
    can_edit = models.BooleanField(blank=False, default=True)

    def __str__(self):
        return f'Team "{self.team}" - {self.qapp}'


class Revision(EpaBaseModel):

    qapp = models.ForeignKey(Qapp, on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=False)
    author = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)


class AcronymAbbreviation(EpaBaseModel):

    qapp = models.ForeignKey(Qapp, on_delete=models.CASCADE)
    acronym_abbreviation = models.TextField(blank=False, null=False)
    definition = models.TextField(blank=False, null=False)

    @property
    def labels(self):
        return {'acronym_abbreviation': 'Acronym/Abbreviation'}
