from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView, TemplateView
import qapp_builder.forms.section_b_forms as forms
from qapp_builder.models import SectionB, SectionB7, HardwareSoftware
from qapp_builder.views.inheritable_views import SectionCreateBase, \
    SectionDetailBase, SectionTemplateView, SectionUpdateBase
from constants.qapp_section_b_const import SECTION_B


class SectionBCreate(SectionCreateBase):

    model = SectionB
    form_class = forms.SectionBForm
    section_title = SECTION_B['b']['header']
    previous_url_name = 'sectiona12_detail'
    detail_url_name = 'sectionb_detail'
    next_url_name = 'sectionb73_detail'

    def form_valid(self, form):
        # Set the qapp field based on the URL path/PK
        form.instance.qapp_id = self.kwargs['qapp_id']
        return super().form_valid(form)


class SectionBUpdate(SectionUpdateBase):

    model = SectionB
    form_class = forms.SectionBForm
    section_title = SECTION_B['b']['header']
    previous_url_name = 'sectionb_detail'
    detail_url_name = 'sectionb_detail'
    next_url_name = 'sectionb73_detail'

    def get_success_url(self):
        return reverse(
            'sectionb_detail', kwargs={'qapp_id': self.kwargs['qapp_id']})


class SectionBDetail(SectionDetailBase):

    model = SectionB
    section_title = SECTION_B['b']['header']
    previous_url_name = 'sectiona12_detail'
    detail_url_name = 'sectionb_detail'
    edit_url_name = 'sectionb_edit'
    create_url_name = 'sectionb_create'
    next_url_name = 'sectionb7_detail'


class SectionB7Create(SectionCreateBase):

    model = SectionB7
    form_class = forms.SectionB7Form
    section_title = SECTION_B['b']['header']
    previous_url_name = 'sectionb_detail'
    detail_url_name = 'sectionb7_detail'
    next_url_name = 'sectionc_detail'

    def form_valid(self, form):
        # Set the qapp field based on the URL path/PK
        form.instance.section_b = SectionB.objects.get(
            qapp_id=self.kwargs['qapp_id'])
        return super().form_valid(form)


class SectionB7Detail(SectionDetailBase):

    model = SectionB7
    template_name = 'qapp/sectionb/b7_detail.html'
    section_title = SECTION_B['b7']['header']
    edit_url_name = 'sectionb7_edit'
    previous_url_name = 'sectionb_detail'
    create_url_name = 'sectionb7_create'
    next_url_name = 'sectionc_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hdw_sfw_list'] = HardwareSoftware.objects.filter(
            qapp_id=self.kwargs['qapp_id'])
        context['b7_label'] = SectionB7().labels['b7']
        context['b71_label'] = SectionB7().labels['b71']
        context['b72_label'] = SectionB7().labels['b72']
        context['b73_label'] = SectionB7().labels['b73']
        context['b74_label'] = SectionB7().labels['b74']
        context['b74_boilerplate'] = SECTION_B['b74']['boilerplate']
        return context


class SectionB7Update(SectionUpdateBase):

    model = SectionB7
    form_class = forms.SectionB7Form
    section_title = SECTION_B['b']['header']
    previous_url_name = 'sectionb7_detail'
    detail_url_name = 'sectionb7_detail'
    next_url_name = 'sectionb7_detail'
