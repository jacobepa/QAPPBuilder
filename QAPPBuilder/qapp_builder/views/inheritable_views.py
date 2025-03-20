from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView, TemplateView
from teams.models import TeamMembership
from qapp_builder.models import Qapp, QappSharingTeamMap
from qapp_builder.views.progress_views import get_qapp_page_list

GENERIC_FORM_TEMPLATE = 'qapp/generic_form.html'
CONFIRM_DELETE_TEMPLATE = 'qapp/confirm_delete.html'


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
    return user.is_superuser or qapp.created_by == user


class SectionTemplateView(LoginRequiredMixin, TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.section_title
        context['previous_url'] = reverse(
            self.previous_url_name, kwargs={'qapp_id': self.kwargs['qapp_id']})
        context['next_url'] = reverse(
            self.next_url_name, kwargs={'qapp_id': self.kwargs['qapp_id']})
        context['qapp_id'] = self.kwargs['qapp_id']
        context['page_list'] = get_qapp_page_list(self.kwargs['qapp_id'])
        context['current_page'] = self.current_page
        return context


class SectionCreateBase(LoginRequiredMixin, CreateView):

    template_name = GENERIC_FORM_TEMPLATE

    def dispatch(self, request, *args, **kwargs):
        # Check if the object already exists
        if self.model.objects.filter(qapp_id=self.kwargs['qapp_id']).exists():
            # Redirect to the detail view if the object exists
            return redirect(reverse(self.detail_url_name,
                                    kwargs={'qapp_id': self.kwargs['qapp_id']}))

        # Check if the user has permissions to contribute to the QAPP:
        qapp = get_object_or_404(Qapp, id=self.kwargs['qapp_id'])
        if not check_can_edit(qapp, request.user):
            return HttpResponse('Unauthorized', status=401)

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.section_title
        context['previous_url'] = reverse(
            self.previous_url_name, kwargs={'qapp_id': self.kwargs['qapp_id']})
        if hasattr(self, 'boilerplate'):
            context['boilerplate'] = self.boilerplate
        if hasattr(self, 'boilerplate_list'):
            context['boilerplate_list'] = self.boilerplate_list
        context['qapp_id'] = self.kwargs['qapp_id']
        context['page_list'] = get_qapp_page_list(self.kwargs['qapp_id'])
        context['current_page'] = self.current_page
        return context

    def form_valid(self, form):
        # Set the qapp field based on the URL path/PK
        form.instance.qapp_id = self.kwargs['qapp_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(self.next_url_name,
                       kwargs={'qapp_id': self.kwargs['qapp_id']})


class SectionUpdateBase(LoginRequiredMixin, UpdateView):

    template_name = GENERIC_FORM_TEMPLATE

    def dispatch(self, request, *args, **kwargs):
        qapp = get_object_or_404(Qapp, id=self.kwargs['qapp_id'])
        if not check_can_edit(qapp, request.user):
            return HttpResponse('Unauthorized', status=401)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.section_title
        context['previous_url'] = reverse(
            self.previous_url_name, kwargs={'qapp_id': self.kwargs['qapp_id']})
        if hasattr(self, 'boilerplate'):
            context['boilerplate'] = self.boilerplate
        if hasattr(self, 'boilerplate_list'):
            context['boilerplate_list'] = self.boilerplate_list
        context['qapp_id'] = self.kwargs['qapp_id']
        context['page_list'] = get_qapp_page_list(self.kwargs['qapp_id'])
        context['current_page'] = self.current_page
        return context

    def get_success_url(self):
        # NOTE: Some issues with the URL's mixing of pk and qapp_id
        #       Going to try to solve that in these base classes
        return reverse(
            self.detail_url_name,
            kwargs={'qapp_id': self.kwargs['qapp_id']})

    def get_object(self):
        # Explicitly retrieve the object based on qapp_id
        obj = get_object_or_404(self.model, qapp_id=self.kwargs['qapp_id'])
        return obj


class SectionDetailBase(LoginRequiredMixin, DetailView):

    template_name = 'qapp/generic_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.section_title
        context['previous_url'] = reverse(
            self.previous_url_name, kwargs={'qapp_id': self.kwargs['qapp_id']})
        context['next_url'] = reverse(
            self.next_url_name, kwargs={'qapp_id': self.kwargs['qapp_id']})
        context['edit_url'] = reverse(
            self.edit_url_name, kwargs={'qapp_id': self.kwargs['qapp_id']})
        context['qapp_id'] = self.kwargs['qapp_id']
        if hasattr(self, 'boilerplate'):
            context['boilerplate'] = self.boilerplate
        if hasattr(self, 'boilerplate_list'):
            context['boilerplate_list'] = self.boilerplate_list
        context['page_list'] = get_qapp_page_list(self.kwargs['qapp_id'])
        context['current_page'] = self.current_page
        return context

    def dispatch(self, request, *args, **kwargs):
        qapp_id = self.kwargs['qapp_id']
        # Check if the object already exists
        if not self.model.objects.filter(qapp_id=qapp_id).exists():
            # Redirect to the desired URL if the object exists
            return redirect(reverse(self.create_url_name,
                                    kwargs={'qapp_id': qapp_id}))
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        # Explicitly retrieve the object based on qapp_id
        obj = get_object_or_404(self.model, qapp_id=self.kwargs['qapp_id'])
        return obj
