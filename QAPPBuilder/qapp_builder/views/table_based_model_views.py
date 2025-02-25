from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# NOTE: Sections A9 and A10 are static/readonly with boilerplate
from qapp_builder.models import SectionA2, AdditionalSignature, \
    AcronymAbbreviation, Distribution, RoleResponsibility, DocumentRecord
import qapp_builder.forms.section_a_forms as forms

GENERIC_FORM_TEMPLATE = 'qapp/generic_form.html'
CONFIRM_DELETE_TEMPLATE = 'qapp/confirm_delete.html'


class AdditionalSignatureBase(LoginRequiredMixin):

    model = AdditionalSignature
    form_class = forms.AdditionalSignatureForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add an Additional Signee'
        context['previous_url'] = reverse(
            'sectiona2_detail', kwargs={'qapp_id': self.kwargs['qapp_id']})
        return context

    def get_success_url(self):
        return reverse('sectiona2_detail',
                       kwargs={'qapp_id': self.kwargs['qapp_id']})


class AdditionalSignatureCreate(AdditionalSignatureBase, CreateView):

    template_name = GENERIC_FORM_TEMPLATE

    def form_valid(self, form):
        qapp_id = self.kwargs['qapp_id']
        # Set the qapp field based on the URL path/PK
        form.instance.section_a2_id = SectionA2.objects.get(qapp_id=qapp_id).id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('sectiona2_detail',
                       kwargs={'qapp_id': self.kwargs['qapp_id']})


class AdditionalSignatureUpdate(AdditionalSignatureBase, UpdateView):

    template_name = GENERIC_FORM_TEMPLATE


class AdditionalSignatureDelete(AdditionalSignatureBase, DeleteView):

    template_name = CONFIRM_DELETE_TEMPLATE


class AcronymAbbreviationBase(LoginRequiredMixin):

    model = AcronymAbbreviation
    form_class = forms.AcronymAbbreviationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add a Definition for an Acronym or Abbreviation'
        context['previous_url'] = reverse(
            'sectiona3_detail', kwargs={'qapp_id': self.kwargs['qapp_id']})
        return context

    def get_success_url(self):
        return reverse('sectiona3_detail',
                       kwargs={'qapp_id': self.kwargs['qapp_id']})


class AcronymAbbreviationCreate(AcronymAbbreviationBase, CreateView):

    template_name = GENERIC_FORM_TEMPLATE

    def form_valid(self, form):
        form.instance.qapp_id = self.kwargs['qapp_id']
        return super().form_valid(form)


class AcronymAbbreviationDelete(AcronymAbbreviationBase, DeleteView):

    template_name = CONFIRM_DELETE_TEMPLATE

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class DistributionBase(LoginRequiredMixin):

    model = Distribution
    form_class = forms.DistributionForm
    template_name = GENERIC_FORM_TEMPLATE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'QAPP Distribution Recipient'
        context['previous_url'] = reverse(
            'sectiona7_detail', kwargs={'qapp_id': self.kwargs['qapp_id']})
        return context

    def get_success_url(self):
        return reverse('sectiona7_detail',
                       kwargs={'qapp_id': self.kwargs['qapp_id']})


class DistributionCreate(DistributionBase, CreateView):

    def form_valid(self, form):
        form.instance.qapp_id = self.kwargs['qapp_id']
        return super().form_valid(form)


class DistributionUpdate(DistributionBase, UpdateView):

    pass


class DistributionDelete(DistributionBase, DeleteView):

    template_name = CONFIRM_DELETE_TEMPLATE

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class RoleResponsibilityBase(LoginRequiredMixin):

    model = RoleResponsibility
    form_class = forms.RoleResponsibilityForm
    template_name = GENERIC_FORM_TEMPLATE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'QAPP Roles and Responsibilities'
        context['previous_url'] = reverse(
            'sectiona8_detail', kwargs={'qapp_id': self.kwargs['qapp_id']})
        return context

    def get_success_url(self):
        return reverse('sectiona8_detail',
                       kwargs={'qapp_id': self.kwargs['qapp_id']})


class RoleResponsibilityCreate(RoleResponsibilityBase, CreateView):

    def form_valid(self, form):
        form.instance.qapp_id = self.kwargs['qapp_id']
        return super().form_valid(form)


class RoleResponsibilityUpdate(RoleResponsibilityBase, UpdateView):

    pass


class RoleResponsibilityDelete(RoleResponsibilityBase, DeleteView):

    template_name = CONFIRM_DELETE_TEMPLATE

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class DocumentRecordBase(LoginRequiredMixin):

    model = DocumentRecord
    form_class = forms.DocumentRecordForm
    template_name = GENERIC_FORM_TEMPLATE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'QAPP Documents and Records'
        context['previous_url'] = reverse(
            'sectiona12_detail', kwargs={'qapp_id': self.kwargs['qapp_id']})
        return context

    def get_success_url(self):
        return reverse('sectiona12_detail',
                       kwargs={'qapp_id': self.kwargs['qapp_id']})


class DocumentRecordCreate(DocumentRecordBase, CreateView):

    def form_valid(self, form):
        form.instance.qapp_id = self.kwargs['qapp_id']
        return super().form_valid(form)


class DocumentRecordUpdate(DocumentRecordBase, UpdateView):

    pass


class DocumentRecordDelete(DocumentRecordBase, DeleteView):

    template_name = CONFIRM_DELETE_TEMPLATE

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
