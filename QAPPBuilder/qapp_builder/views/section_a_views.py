from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from qapp_builder.models import SectionA1, SectionA2, SectionA, Qapp
import qapp_builder.forms.section_a_forms as forms


class SectionA1Create(LoginRequiredMixin, CreateView):

  model = SectionA1
  form_class = forms.SectionA1Form
  template_name = 'qapp/sectiona/a1_form.html'

  def get_context_data(self, **kwargs):
    data = super().get_context_data(**kwargs)
    if self.request.POST:
      data['version_formset'] = forms.VersionControlFormSet(self.request.POST)
    else:
      data['version_formset'] = forms.VersionControlFormSet()
    return data

  def form_valid(self, form):
    qapp = Qapp.objects.get(pk=self.kwargs['pk'])
    section_a, created = SectionA.objects.get_or_create(qapp=qapp)
    form.instance.section_a = section_a
    context = self.get_context_data()
    version_formset = context['version_formset']
    if form.is_valid() and version_formset.is_valid():
      self.object = form.save()
      version_formset.instance = self.object
      version_formset.save()
      return redirect(self.get_success_url())
    else:
      return self.render_to_response(self.get_context_data(form=form))

  def get_success_url(self):
    return reverse('sectiona2_create', kwargs={'pk': self.kwargs['pk']})


class SectionA1Update(LoginRequiredMixin, UpdateView):

  model = SectionA1
  form_class = forms.SectionA1Form
  template_name = 'qapp/sectiona/a1_form.html'

  def get_context_data(self, **kwargs):
    data = super().get_context_data(**kwargs)
    if self.request.POST:
      data['version_formset'] = forms.VersionControlFormSet(
        self.request.POST, instance=self.object)
    else:
      data['version_formset'] = forms.VersionControlFormSet(
        instance=self.object)
    return data

  def form_valid(self, form):
    context = self.get_context_data()
    version_formset = context['version_formset']
    if form.is_valid() and version_formset.is_valid():
      self.object = form.save()
      version_formset.instance = self.object
      version_formset.save()
      return redirect(self.get_success_url())
    else:
      return self.render_to_response(self.get_context_data(form=form))

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
    return reverse('sectiona3_create', kwargs={'pk': self.kwargs['pk']})

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