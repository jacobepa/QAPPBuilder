from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView, TemplateView

GENERIC_FORM_TEMPLATE = 'qapp/generic_form.html'
CONFIRM_DELETE_TEMPLATE = 'qapp/confirm_delete.html'


class SectionTemplateView(LoginRequiredMixin, TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.section_title
        context['previous_url'] = reverse(
            self.previous_url_name, kwargs={'qapp_id': self.kwargs['qapp_id']})
        context['next_url'] = reverse(
            self.next_url_name, kwargs={'qapp_id': self.kwargs['qapp_id']})
        return context


class SectionCreateBase(LoginRequiredMixin, CreateView):

    template_name = GENERIC_FORM_TEMPLATE

    def dispatch(self, request, *args, **kwargs):
        # Check if the object already exists
        if self.model.objects.filter(qapp_id=self.kwargs['qapp_id']).exists():
            # Redirect to the detail view if the object exists
            return redirect(reverse(self.detail_url_name,
                                    kwargs={'qapp_id': self.kwargs['qapp_id']}))
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.section_title
        context['previous_url'] = reverse(
            self.previous_url_name, kwargs={'qapp_id': self.kwargs['qapp_id']})
        if hasattr(self, 'boilerplate'):
            context['boilerplate'] = self.boilerplate
        if hasattr(self, 'boilerplate_list'):
            context['boilerplate_list'] = self.boilerplate_list
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
