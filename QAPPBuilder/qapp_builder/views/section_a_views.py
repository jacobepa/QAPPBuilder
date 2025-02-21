from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView, TemplateView
from qapp_builder.models import SectionA1, SectionA2, SectionA4, Qapp
import qapp_builder.forms.section_a_forms as forms


class SectionA1Create(LoginRequiredMixin, CreateView):

    model = SectionA1
    form_class = forms.SectionA1Form
    template_name = 'qapp/sectiona/a1_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Section A.1'
        context['previous_url'] = reverse('qapp_detail', kwargs=self.kwargs)
        return context

    def form_valid(self, form):
        qapp = Qapp.objects.get(pk=self.kwargs['pk'])
        # Get corresponding section A or create if it doesn't exist yet.
        context = self.get_context_data()
        # Get the version control formset
        version_formset = context['version_formset']
        # Check that the SectionA1 and VersionControl forms are valid
        if form.is_valid() and version_formset.is_valid():
            self.object = form.save()
            version_formset.instance = self.object
            version_formset.save()
            for version in version_formset:
                if version.is_valid():
                    version.instance.qapp_id = qapp.id
                    version.instance.section_a1 = self.object
                    version.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('sectiona2_create', kwargs={'pk': self.kwargs['pk']})
