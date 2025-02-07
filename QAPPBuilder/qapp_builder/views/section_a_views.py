from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from qapp_builder.models import SectionA1, SectionA, Qapp

import qapp_builder.forms.section_a_forms as forms


class SectionA1CreateView(LoginRequiredMixin, CreateView):
  model = SectionA1
  form_class = forms.SectionA1Form
  template_name = 'section_a1_form.html'
  success_url = reverse_lazy('section_a1_list')

  def form_valid(self, form):
    # Retrieve or create the parent SectionA
    qapp = Qapp.objects.get(pk=self.kwargs['qapp_id'])
    section_a, created = SectionA.objects.get_or_create(qapp=qapp)
    form.instance.section_a = section_a  # Assign the parent SectionA
    self.object = form.save()
    return super().form_valid(form)
