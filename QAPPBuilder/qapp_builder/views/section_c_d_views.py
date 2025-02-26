from django.urls import reverse
import qapp_builder.forms.section_c_d_forms as forms
from qapp_builder.models import SectionC, SectionD, SectionA1
from qapp_builder.views.inheritable_views import SectionCreateBase, \
    SectionDetailBase, SectionUpdateBase
from constants.qapp_section_a_const import QA_CATEGORY_A
from constants.qapp_section_c_d_const import SECTION_C, SECTION_D


class SectionCCreate(SectionCreateBase):

    model = SectionC
    form_class = forms.SectionCForm
    section_title = SECTION_C['c']['header']
    previous_url_name = 'sectionb7_detail'
    detail_url_name = 'sectionc_detail'
    next_url_name = 'sectiond_detail'

    def form_valid(self, form):
        # Set the qapp field based on the URL path/PK
        form.instance.qapp_id = self.kwargs['qapp_id']
        return super().form_valid(form)


class SectionCDetail(SectionDetailBase):

    model = SectionC
    template_name = 'qapp/sectionc/c_detail.html'
    section_title = SECTION_C['c']['header']
    edit_url_name = 'sectionc_edit'
    previous_url_name = 'sectionb7_detail'
    create_url_name = 'sectionc_create'
    next_url_name = 'sectiond_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['c1_label'] = SECTION_C['c1']['header']
        context['c11_label'] = SECTION_C['c11']['header']
        context['c12_label'] = SECTION_C['c12']['header']
        context['c12_boilerplate'] = SECTION_C['c12']['boilerplate']
        context['c2_label'] = SECTION_C['c2']['header']
        qa_category = SectionA1.objects.get(
            qapp_id=self.kwargs['qapp_id']).qa_category
        if qa_category is QA_CATEGORY_A:
            context['c11_boilerplate'] = SECTION_C['c11']['boilerplate_a']
        else:
            context['c11_boilerplate'] = SECTION_C['c11']['boilerplate_b']
        return context


class SectionCUpdate(SectionUpdateBase):

    model = SectionC
    form_class = forms.SectionCForm
    section_title = SECTION_C['c']['header']
    previous_url_name = 'sectionc_detail'
    detail_url_name = 'sectionc_detail'
    next_url_name = 'sectionc_detail'


class SectionDCreate(SectionCreateBase):

    model = SectionD
    form_class = forms.SectionDForm
    section_title = SECTION_D['d']['header']
    previous_url_name = 'sectionc_detail'
    detail_url_name = 'sectiond_detail'
    next_url_name = 'qapp_detail'

    def form_valid(self, form):
        # Set the qapp field based on the URL path/PK
        form.instance.qapp_id = self.kwargs['qapp_id']
        return super().form_valid(form)


class SectionDUpdate(SectionUpdateBase):

    model = SectionD
    form_class = forms.SectionDForm
    section_title = SECTION_D['d']['header']
    previous_url_name = 'sectiond_detail'
    detail_url_name = 'sectiond_detail'
    next_url_name = 'sectiond_detail'

    def get_success_url(self):
        return reverse(
            'sectiond_detail', kwargs={'qapp_id': self.kwargs['qapp_id']})


class SectionDDetail(SectionDetailBase):

    model = SectionD
    section_title = SECTION_D['d']['header']
    previous_url_name = 'sectionc_detail'
    detail_url_name = 'sectiond_detail'
    edit_url_name = 'sectiond_edit'
    create_url_name = 'sectiond_create'
    next_url_name = 'qapp_detail'
