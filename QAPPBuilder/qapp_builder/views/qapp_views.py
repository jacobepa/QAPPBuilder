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
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, ListView, \
    TemplateView, UpdateView
from django.contrib.auth.models import User
from qapp_builder.forms.qapp_forms import QappForm
from qapp_builder.models import Qapp, QappSharingTeamMap, SectionA1
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
    #       a9_clean = a9_clean.replace('QA Category A', sect.qapp.qa_category)
    #   else:
    #       a9_clean = a9_clean.replace('QA Category B', sect.qapp.qa_category)
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

    template_name = 'qapp/qapp_index.html'

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


# NOTE: Not sure how to get this working, so commenting out for now.
#       This is more of an optimization design anyway, so not necessary.
# class EpaNavAbstractView():

#   def get_context_data(self):
#     context = {}
#     # Add custom context here
#     context['title'] = self.title
#     context['edit_url'] = self.edit_url
#     # TODO: Figure out where this request came from originally (user or team)
#     context['previous_url'] = self.previous_url
#     context['next_url'] = self.next_url
#     return context


class QappCreateView(LoginRequiredMixin, CreateView):
    model = Qapp
    form_class = QappForm
    template_name = 'qapp/qapp_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['previous_url'] = f'/qapp/list/user/{self.request.user.id}/'
        return context

    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Auto-fill created_by
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('sectiona1_create', kwargs={'pk': self.object.id})


class QappList(LoginRequiredMixin, ListView):
    """Class for listing this user's (or all if admin) QAPP objects."""

    model = Qapp
    template_name = 'qapp/qapp_list.html'
    context_object_name = 'qapp_list'

    def get_context_data(self, **kwargs):
        """
        Override the default method to send data to the template.

        Specifically, include the user or team information
        for this list of data.
        """
        context = super().get_context_data(**kwargs)
        path = self.request.path.split('/')
        p_id = path[len(path) - 1]
        p_type = path[len(path) - 2]
        if p_type == 'user':
            context['p_user'] = User.objects.get(id=p_id)
        elif p_type == 'team':
            context['team'] = Team.objects.get(id=p_id)
        return context

    def get_queryset(self):
        """Get a list of QAPP objects based on the provided user or team ID."""
        path = self.request.path.split('/')
        p_id = path[len(path) - 1]
        p_type = path[len(path) - 2]
        if p_type == 'user':
          return get_qar5_for_user(p_id)
        if p_type == 'team':
          return get_qar5_for_team(p_id)
        return get_qapp_all()


class QappDetail(LoginRequiredMixin, DetailView):
    """Class for viewing an existing QAPP."""

    model = Qapp
    # template_name = 'qapp/qapp_detail.html'
    template_name = 'qapp/qapp_overview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['sectiona1'] = SectionA1.objects.filter(
            qapp=self.object).first()
        context['edit_url'] = reverse('qapp_edit',
                                      kwargs={'pk': self.object.id})
        # TODO: Figure out where this request came from (user or team)
        context['previous_url'] = reverse(
            'qapp_list_user', kwargs={'user_id': self.request.user.id})
        context['next_url'] = reverse('sectiona1_detail',
                                      kwargs={'qapp_id': self.object.id})
        return context


class QappUpdate(LoginRequiredMixin, UpdateView):
    """Class for editing an existing (newly created) QAPP."""

    model = Qapp
    form_class = QappForm
    template_name = 'qapp/qapp_form.html'

    def get_success_url(self):
        return reverse_lazy('qapp_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add custom context here
        context['title'] = 'Edit QAPP'
        context['previous_url'] = f'/qapp/{self.object.id}/detail/'
        return context
