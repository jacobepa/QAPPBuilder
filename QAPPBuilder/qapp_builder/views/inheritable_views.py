from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView, TemplateView

GENERIC_FORM_TEMPLATE = 'qapp/generic_form.html'
CONFIRM_DELETE_TEMPLATE = 'qapp/confirm_delete.html'

QAPP_PAGE_INDEX = {
    'qapp': 0,
    'section-a1': 1,
    'section-a2': 2,
    'section-a3': 3,
    'section-a4': 4,
    'section-a5': 5,
    'section-a6': 6,
    'section-a7': 7,
    'section-a8': 8,
    'section-a9': 9,
    'section-a10': 10,
    'section-a11': 11,
    'section-a12': 12,
    'section-b': 13,
    'section-b7': 14,
    'section-c': 15,
    'section-d': 16
}


def get_qapp_page_list():
    return [
        {'tail_path': '/detail/', 'label': 'QAPP Details'},
        {'tail_path': '/section-a1/detail/', 'label': 'Section A1'},
        {'tail_path': '/section-a2/detail/', 'label': 'Section A2'},
        {'tail_path': '/section-a3/detail/', 'label': 'Section A3'},
        {'tail_path': '/section-a4/detail/', 'label': 'Section A4'},
        {'tail_path': '/section-a5/detail/', 'label': 'Section A5'},
        {'tail_path': '/section-a6/detail/', 'label': 'Section A6'},
        {'tail_path': '/section-a7/', 'label': 'Section A7'},
        {'tail_path': '/section-a8/', 'label': 'Section A8'},
        {'tail_path': '/section-a9/', 'label': 'Section A9'},
        {'tail_path': '/section-a10/detail/', 'label': 'Section A10'},
        {'tail_path': '/section-a11/detail/', 'label': 'Section A11'},
        {'tail_path': '/section-a12/', 'label': 'Section A12'},
        {'tail_path': '/section-b/detail/', 'label': 'Section B'},
        {'tail_path': '/section-b7/detail/', 'label': 'Section B7'},
        {'tail_path': '/section-c/detail/', 'label': 'Section C'},
        {'tail_path': '/section-d/detail/', 'label': 'Section D'}
    ]


class SectionTemplateView(LoginRequiredMixin, TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.section_title
        context['previous_url'] = reverse(
            self.previous_url_name, kwargs={'qapp_id': self.kwargs['qapp_id']})
        context['next_url'] = reverse(
            self.next_url_name, kwargs={'qapp_id': self.kwargs['qapp_id']})
        context['qapp_id'] = self.kwargs['qapp_id']
        context['page_list'] = get_qapp_page_list()
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
        context['page_list'] = get_qapp_page_list()
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
        context['page_list'] = get_qapp_page_list()
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
        context['page_list'] = get_qapp_page_list()
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
