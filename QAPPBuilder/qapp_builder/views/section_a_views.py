from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView, TemplateView
from qapp_builder.models import SectionA1, SectionA2, SectionA4, SectionA, Qapp
import qapp_builder.forms.section_a_forms as forms


class SectionA1Create(LoginRequiredMixin, CreateView):
  model = SectionA1
  form_class = forms.SectionA1Form
  template_name = 'qapp/sectiona/a1_form.html'

  def get_success_url(self):
    return reverse('sectiona2_create', kwargs={'pk': self.kwargs['pk']})

  def form_valid(self, form):
    qapp = Qapp.objects.get(pk=self.kwargs['pk'])
    section_a, created = SectionA.objects.get_or_create(qapp=qapp)
    form.instance.section_a = section_a
    self.object = form.save()
    return super().form_valid(form)


class SectionA1Update(LoginRequiredMixin, UpdateView):
  model = SectionA1
  form_class = forms.SectionA1Form
  template_name = 'qapp/sectiona/a1_form.html'

  def get_success_url(self):
    return reverse('sectiona2_update', kwargs={'pk': self.kwargs['pk']})


class SectionA1Detail(LoginRequiredMixin, DetailView):
  model = SectionA1
  template_name = 'qapp/sectiona/a1_detail.html'

  def get_object(self, queryset=None):
    qapp_id = self.kwargs['pk']
    return SectionA1.objects.filter(section_a__qapp_id=qapp_id).first() or None

  def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    if self.object is None:
      return HttpResponseRedirect(reverse('sectiona1_create', kwargs=kwargs))
    return super().get(request, *args, **kwargs)


class SectionA2Create(LoginRequiredMixin, CreateView):
  model = SectionA2
  form_class = forms.SectionA2Form
  template_name = 'qapp/sectiona/a2_form.html'

  def get_success_url(self):
    return reverse('sectiona5_create', kwargs={'pk': self.kwargs['pk']})

  def form_valid(self, form):
    qapp = Qapp.objects.get(pk=self.kwargs['pk'])
    section_a = SectionA.objects.get(qapp=qapp)
    form.instance.section_a = section_a
    self.object = form.save()
    return super().form_valid(form)


class SectionA2Update(LoginRequiredMixin, UpdateView):
  model = SectionA2
  form_class = forms.SectionA2Form
  template_name = 'qapp/sectiona/a2_form.html'

  def get_success_url(self):
    return reverse('sectiona3_update', kwargs={'pk': self.kwargs['pk']})


class SectionA2Detail(LoginRequiredMixin, DetailView):
  model = SectionA2
  template_name = 'qapp/sectiona/a2_detail.html'
  context_object_name = 'section_a2'

  def get_object(self, queryset=None):
    try:
      qapp = Qapp.objects.get(pk=self.kwargs['pk'])
      section_a2 = SectionA2.objects.get(section_a__qapp=qapp)
      return section_a2
    except SectionA2.DoesNotExist:
      return None

  def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    if self.object is None:
      return reverse('sectiona2_create', kwargs={'pk': self.kwargs['pk']})
    return super().get(request, *args, **kwargs)


class SectionA3Page(LoginRequiredMixin, TemplateView):
  """Class to return the first page of the Existing Data flow."""

  template_name = 'qapp/sectiona/a3.html'


class SectionA4Create(LoginRequiredMixin, CreateView):
  model = SectionA4
  form_class = forms.SectionA2Form
  template_name = 'qapp/sectiona/a4_form.html'

  def get_success_url(self):
    return reverse('sectiona3_page', kwargs={'pk': self.kwargs['pk']})

  def form_valid(self, form):
    qapp = Qapp.objects.get(pk=self.kwargs['pk'])
    section_a = SectionA.objects.get(qapp=qapp)
    form.instance.section_a = section_a
    self.object = form.save()
    return super().form_valid(form)


class SectionA4Update(LoginRequiredMixin, UpdateView):
  model = SectionA4
  form_class = forms.SectionA4Form
  template_name = 'qapp/sectiona/a4_form.html'

  def get_success_url(self):
    return reverse('sectiona3_update', kwargs={'pk': self.kwargs['pk']})


class SectionA4Detail(LoginRequiredMixin, DetailView):
  model = SectionA4
  template_name = 'qapp/sectiona/a4_detail.html'
  context_object_name = 'section_a4'

  def get_object(self, queryset=None):
    try:
      qapp = Qapp.objects.get(pk=self.kwargs['pk'])
      section_a4 = SectionA4.objects.get(section_a__qapp=qapp)
      return section_a4
    except SectionA4.DoesNotExist:
      return None

  def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    if self.object is None:
      return reverse('sectiona4_create', kwargs={'pk': self.kwargs['pk']})
    return super().get(request, *args, **kwargs)

