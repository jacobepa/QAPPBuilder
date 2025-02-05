# views.py (qapp_builder)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# py-lint: disable=C0301,E1101,R0901,W0613,W0622,C0411


"""Definition of views."""

from datetime import datetime
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .models import Qapp, QappSharingTeamMap
from teams.models import Team, TeamMembership


@login_required
@staff_member_required
def web_dev_tools(request, *args, **kwargs):
  """
  Go to the web developer page with custom admin functionality.

  - Includes various custom admin functionality.
  - Includes button to remove extra new line characters/spaces from QAPP data
  """
  return render(request, 'web_dev.html', {})


@login_required
@staff_member_required
def clean_qapps(request, *args, **kwargs):
  """
  Clean QAPP Data.

  - Remove extra new line characters and spaces.
  - Convert QA_Category to the proper value.
  """
  # sections_a = SectionA.objects.all()
  # for sect in sections_a:
  #   # Clean Section A
  #   a3_clean = sect.a3.replace('\r\n', ' ').replace('  ', ' ')
  #   a9_clean = sect.a9.replace('\r\n', ' ').replace('  ', ' ')
  #   a9_clean = a9_clean.replace('QA QA', 'QA')
  #   if 'B' in sect.qapp.qa_category:
  #     a9_clean = a9_clean.replace('QA Category A', sect.qapp.qa_category)
  #   else:
  #     a9_clean = a9_clean.replace('QA Category B', sect.qapp.qa_category)
  #   sect.a3 = a3_clean
  #   sect.a9 = a9_clean
  #   sect.save()
  return render(request, 'web_dev.html', {})


def contact(request):
  """Render the contact page."""
  assert isinstance(request, HttpRequest)
  return render(
    request,
    'main/contact.html',
    {
      'title': 'Contact',
      'year': datetime.now().year,
    }
  )


def get_qapp_all():
  """Get all QAPP data regardless of user or team."""
  return Qapp.objects.all()


def check_can_edit(qapp, user):
  """
  Check if the provided user can edit the provided qapp.

  All of the user's member teams are checked as well as the user's
  super user status or qapp ownership status.
  """
  # Check if any of the user's teams have edit privilege:
  user_teams = TeamMembership.objects.filter(
    member=user).values_list('team', flat=True)

  for team in user_teams:
    data_team_map = QappSharingTeamMap.objects.filter(
      qapp=qapp, team=team).first()
    if data_team_map and data_team_map.can_edit:
      return True

  # Check if the user is super or owns the qapp:
  return user.is_superuser or qapp.prepared_by == user


class QappIndex(LoginRequiredMixin, TemplateView):
  """Class to return the first page of the Existing Data flow."""

  template_name = 'qapp_index.html'

  def get_context_data(self, **kwargs):
    """
    Override default method to send data to the template.

    Specifically, want to send a list of users and teams to select from.
    """
    context = super().get_context_data(**kwargs)
    context['users'] = User.objects.all()
    context['teams'] = Team.objects.all()
    return context


def get_qar5_for_user(user_id, qapp_id=None):
  """Get all qapps created by a User."""
  user = User.objects.get(id=user_id)
  if qapp_id:
    return Qapp.objects.filter(id=qapp_id)
  return Qapp.objects.filter(prepared_by=user)


def get_qar5_for_team(team_id, qapp_id=None):
  """Get all data belonging to a team."""
  team = Team.objects.get(id=team_id)
  include_qapps = QappSharingTeamMap.objects.filter(
    team=team).values_list('qapp', flat=True)

  if qapp_id:
    return Qapp.objects.filter(
      id__in=include_qapps).filter(id=qapp_id).first()

  return Qapp.objects.filter(id__in=include_qapps)
