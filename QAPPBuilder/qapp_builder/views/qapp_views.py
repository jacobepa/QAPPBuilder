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
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, ListView, \
    TemplateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from qapp_builder.forms.qapp_forms import QappForm, RevisionForm
from qapp_builder.models import Qapp, QappSharingTeamMap, SectionA1, Revision, \
    SectionA2, SectionA4, SectionA5, SectionA6, SectionA10, SectionA11, \
    SectionB, SectionB7, SectionC, SectionD
from qapp_builder.views.export_views import export_qapp_docx, export_qapp_pdf
from qapp_builder.views.progress_views import QAPP_PAGE_INDEX, \
    get_qapp_page_list
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


class QappCreateView(LoginRequiredMixin, CreateView):
    model = Qapp
    form_class = QappForm
    template_name = 'qapp/qapp_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['previous_url'] = f'/qapp/list/user/{self.request.user.id}/'
        # context['page_list'] = get_qapp_page_list()
        context['current_page'] = QAPP_PAGE_INDEX['qapp']
        return context

    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Auto-fill created_by
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('sectiona1_create',
                            kwargs={'qapp_id': self.object.id})


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
        context['revisions'] = Revision.objects.filter(qapp_id=self.object.id)
        context['page_list'] = get_qapp_page_list(self.object.id)
        context['current_page'] = QAPP_PAGE_INDEX['qapp']
        context['qapp_id'] = self.object.id
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
        context['qapp_id'] = self.object.id
        return context


class QappDelete(LoginRequiredMixin, DeleteView):

    model = Qapp
    template_name = 'qapp/confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['previous_url'] = reverse(
            'qapp_detail', kwargs={'pk': self.kwargs['pk']})
        return context

    def get_success_url(self):
        # TODO: Figure out where this request came from (user or team)
        return reverse(
            'qapp_list_user', kwargs={'user_id': self.request.user.id})


class RevisionFormBase(LoginRequiredMixin):

    model = Revision
    form_class = RevisionForm
    template_name = 'qapp/generic_form.html'

    def get_success_url(self):
        return reverse_lazy(
            'qapp_detail', kwargs={'pk': self.kwargs['qapp_id']})


class RevisionCreate(RevisionFormBase, CreateView):

    def form_valid(self, form):
        form.instance.qapp_id = self.kwargs['qapp_id']
        self.object = form.save()
        return super().form_valid(form)


class RevisionUpdate(RevisionFormBase, UpdateView):

    pass


class RevisionDelete(RevisionFormBase, DeleteView):

    template_name = 'qapp/confirm_delete.html'

    def post(self, request, *args, **kwargs):
        print('POST')
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


@login_required
def export_qapp(request, *args, **kwargs):

    assert isinstance(request, HttpRequest)
    file_format = request.GET.get('format')
    if str.lower(file_format) == 'pdf':
        return export_qapp_pdf(request, kwargs['pk'])
    return export_qapp_docx(request, kwargs['pk'])


@login_required
def qapp_progress_view(request, *args, **kwargs):
    """
    View to render a QAPP Progress page. Can also be used to navigate to
    specific sections of the QAPP without needing the forward/backward buttons.
    """
    assert isinstance(request, HttpRequest)
    qapp_id = kwargs['pk']
    ctx = {}
    # #########################################################################
    # Section A ---------------------------------------------------------------
    section_a1 = SectionA1.objects.get(qapp_id=qapp_id)  # noqa: F841
    section_a2 = SectionA2.objects.get(qapp_id=qapp_id)  # noqa: F841
    # TODO: SectionA3 doesn't have a model, how to decide its "completeness"?
    section_a4 = SectionA4.objects.get(qapp_id=qapp_id)  # noqa: F841
    section_a5 = SectionA5.objects.get(qapp_id=qapp_id)  # noqa: F841
    section_a6 = SectionA6.objects.get(qapp_id=qapp_id)  # noqa: F841
    # TODO: SectionA7 doesn't have a model, how to decide its "completeness"?
    # TODO: SectionA8 doesn't have a model, how to decide its "completeness"?
    # TODO: SectionA9 doesn't have a model, how to decide its "completeness"?
    section_a10 = SectionA10.objects.get(qapp_id=qapp_id)  # noqa: F841
    section_a11 = SectionA11.objects.get(qapp_id=qapp_id)  # noqa: F841
    # TODO: SectionA12 doesn't have a model, how to decide its "completeness"?
    # #########################################################################
    # Section B ---------------------------------------------------------------
    section_b = SectionB.objects.get(qapp_id=qapp_id)  # noqa: F841
    section_b7 = SectionB7.objects.get(qapp_id=qapp_id)  # noqa: F841
    # #########################################################################
    # Section C ---------------------------------------------------------------
    section_c = SectionC.objects.get(qapp_id=qapp_id)  # noqa: F841
    # #########################################################################
    # Section D ---------------------------------------------------------------
    section_d = SectionD.objects.get(qapp_id=qapp_id)  # noqa: F841
    # #########################################################################
    return render(request, 'qapp/progress.html', ctx)
