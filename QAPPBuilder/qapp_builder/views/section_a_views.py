from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView, TemplateView
from qapp_builder.models import SectionA1, SectionA2, SectionA4, Qapp
import qapp_builder.forms.section_a_forms as forms


class SectionCreateBase(LoginRequiredMixin, CreateView):
    template_name = 'qapp/sectiona/section_form.html'

    def dispatch(self, request, *args, **kwargs):
        # Check if the object already exists
        if self.model.objects.filter(qapp_id=self.kwargs['pk']).exists():
            # Redirect to the detail view if the object exists
            return redirect(reverse(self.detail_url_name,
                                    kwargs={'pk': self.kwargs['pk']}))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.section_title
        context['previous_url'] = reverse(self.previous_url_name,
                                          kwargs=self.kwargs)
        return context

    def form_valid(self, form):
        # Set the qapp field based on the URL path/PK
        form.instance.qapp_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(self.next_url_name, kwargs={'pk': self.object.qapp.pk})


class SectionA1Create(LoginRequiredMixin, CreateView):

    model = SectionA1
    form_class = forms.SectionA1Form
    template_name = 'qapp/sectiona/a1_form.html'

    def dispatch(self, request, *args, **kwargs):
        # Check if the object already exists
        if SectionA1.objects.filter(qapp_id=self.kwargs['pk']).exists():
            # Redirect to the desired URL if the object exists
            return redirect(reverse('sectiona1_detail',
                                    kwargs={'pk': self.kwargs['pk']}))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Section A.1'
        context['previous_url'] = reverse('qapp_detail', kwargs=self.kwargs)
        return context

    def form_valid(self, form):
        # Set the qapp field based on the URL path/PK
        form.instance.qapp_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('sectiona2_create', kwargs={'pk': self.object.qapp.id})


class SectionA1Detail(LoginRequiredMixin, DetailView):

    model = SectionA1
    template_name = 'qapp/sectiona/a1_detail.html'

    def dispatch(self, request, *args, **kwargs):
        # Check if the object already exists
        if not SectionA1.objects.filter(qapp_id=self.kwargs['pk']).exists():
            # Redirect to the desired URL if the object exists
            return redirect(reverse('sectiona1_create',
                                    kwargs={'pk': self.kwargs['pk']}))
        return super().dispatch(request, *args, **kwargs)


class SectionA2Create(LoginRequiredMixin, CreateView):

    model = SectionA2
    form_class = forms.SectionA2Form
    template_name = 'qapp/sectiona/a2_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Section A.2'
        context['previous_url'] = reverse('sectiona1_detail',
                                          kwargs=self.kwargs)
        return context

    def get_success_url(self):
        return reverse('sectiona3_create', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        # Set the qapp field based on the URL path/PK
        form.instance.qapp_id = self.kwargs['pk']
        return super().form_valid(form)


class SectionA2Detail(LoginRequiredMixin, DetailView):

    model = SectionA2
    template_name = 'qapp/sectiona/a2_detail.html'

    def dispatch(self, request, *args, **kwargs):
        # Check if the object already exists
        if not SectionA2.objects.filter(qapp_id=self.kwargs['pk']).exists():
            # Redirect to the desired URL if the object exists
            return redirect(reverse('sectiona2_create',
                                    kwargs={'pk': self.kwargs['pk']}))
        return super().dispatch(request, *args, **kwargs)
