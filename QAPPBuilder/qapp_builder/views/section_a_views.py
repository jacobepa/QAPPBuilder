from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
# NOTE: Sections A9 and A10 are static/readonly with boilerplate
from qapp_builder.models import SectionA1, SectionA2, SectionA4, \
    SectionA5, SectionA6, SectionA11, DocumentRecord, RoleResponsibility, \
    AdditionalSignature, AcronymAbbreviation, Distribution, SectionA10
import qapp_builder.forms.section_a_forms as forms
from qapp_builder.views.inheritable_views import SectionCreateBase, \
    SectionDetailBase, SectionTemplateView, SectionUpdateBase
from qapp_builder.views.progress_views import QAPP_PAGE_INDEX
from constants.qapp_section_a_const import SECTION_A


GENERIC_FORM_TEMPLATE = 'qapp/generic_form.html'
CONFIRM_DELETE_TEMPLATE = 'qapp/confirm_delete.html'


class SectionA1Create(SectionCreateBase):

    model = SectionA1
    form_class = forms.SectionA1Form
    template_name = 'qapp/sectiona/a1_form.html'
    section_title = SECTION_A['a1']['header']
    previous_url_name = 'qapp_detail'
    detail_url_name = 'sectiona1_detail'
    next_url_name = 'sectiona2_create'
    current_page = QAPP_PAGE_INDEX['section-a1']


class SectionA1Update(SectionUpdateBase):

    model = SectionA1
    form_class = forms.SectionA1Form
    template_name = 'qapp/sectiona/a1_form.html'
    section_title = SECTION_A['a1']['header']
    previous_url_name = 'qapp_detail'
    detail_url_name = 'sectiona1_detail'
    next_url_name = 'sectiona2_create'
    current_page = QAPP_PAGE_INDEX['section-a1']


class SectionA1Detail(SectionDetailBase):

    model = SectionA1
    template_name = 'qapp/sectiona/a1_detail.html'
    section_title = SECTION_A['a1']['header']
    edit_url_name = 'sectiona1_edit'
    create_url_name = 'sectiona1_create'
    previous_url_name = 'qapp_detail'
    next_url_name = 'sectiona2_detail'
    current_page = QAPP_PAGE_INDEX['section-a1']


class SectionA2Create(SectionCreateBase):

    model = SectionA2
    form_class = forms.SectionA2Form
    section_title = SECTION_A['a2']['header']
    previous_url_name = 'sectiona1_detail'
    detail_url_name = 'sectiona2_detail'
    next_url_name = 'sectiona3_create'
    current_page = QAPP_PAGE_INDEX['section-a2']


class SectionA2Update(SectionUpdateBase):

    model = SectionA2
    form_class = forms.SectionA2Form
    template_name = 'qapp/sectiona/a2_form.html'
    section_title = SECTION_A['a2']['header']
    previous_url_name = 'sectiona1_detail'
    detail_url_name = 'sectiona2_detail'
    next_url_name = 'sectiona3_create'
    current_page = QAPP_PAGE_INDEX['section-a2']


class SectionA2Detail(SectionDetailBase):

    model = SectionA2
    template_name = 'qapp/sectiona/a2_detail.html'
    section_title = SECTION_A['a2']['header']
    edit_url_name = 'sectiona2_edit'
    create_url_name = 'sectiona2_create'
    previous_url_name = 'sectiona1_detail'
    next_url_name = 'sectiona3_detail'
    current_page = QAPP_PAGE_INDEX['section-a2']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['additional_signatures'] = AdditionalSignature.objects.filter(
            section_a2_id=self.object.id)
        return context


class SectionA3Detail(SectionTemplateView):

    template_name = 'qapp/sectiona/a3_detail.html'
    section_title = SECTION_A['a3']['header']
    edit_url_name = 'sectiona3_edit'
    create_url_name = 'sectiona3_create'
    previous_url_name = 'sectiona2_detail'
    next_url_name = 'sectiona4_detail'
    current_page = QAPP_PAGE_INDEX['section-a3']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.section_title
        context['previous_url'] = reverse(
            self.previous_url_name, kwargs={'qapp_id': self.kwargs['qapp_id']})
        context['next_url'] = reverse(
            self.next_url_name, kwargs={'qapp_id': self.kwargs['qapp_id']})
        context['acronym_abbreviations'] = AcronymAbbreviation.objects.filter(
            qapp_id=self.kwargs['qapp_id'])
        context['qapp_id'] = self.kwargs['qapp_id']

        return context


class SectionA4Create(SectionCreateBase):
    model = SectionA4
    form_class = forms.SectionA4Form
    section_title = SECTION_A['a4']['header']
    previous_url_name = 'sectiona3_detail'
    detail_url_name = 'sectiona4_detail'
    next_url_name = 'sectiona5_create'
    current_page = QAPP_PAGE_INDEX['section-a4']


class SectionA4Update(SectionUpdateBase):
    model = SectionA4
    form_class = forms.SectionA4Form
    section_title = SECTION_A['a4']['header']
    previous_url_name = 'sectiona3_detail'
    detail_url_name = 'sectiona4_detail'
    next_url_name = 'sectiona5_create'
    current_page = QAPP_PAGE_INDEX['section-a4']


class SectionA4Detail(SectionDetailBase):
    model = SectionA4
    section_title = SECTION_A['a4']['header']
    edit_url_name = 'sectiona4_edit'
    create_url_name = 'sectiona4_create'
    previous_url_name = 'sectiona3_detail'
    next_url_name = 'sectiona5_detail'
    current_page = QAPP_PAGE_INDEX['section-a4']


class SectionA5Create(SectionCreateBase):
    model = SectionA5
    form_class = forms.SectionA5Form
    section_title = SECTION_A['a5']['header']
    previous_url_name = 'sectiona4_detail'
    detail_url_name = 'sectiona5_detail'
    next_url_name = 'sectiona6_create'
    current_page = QAPP_PAGE_INDEX['section-a5']


class SectionA5Update(SectionUpdateBase):
    model = SectionA5
    form_class = forms.SectionA5Form
    section_title = SECTION_A['a5']['header']
    previous_url_name = 'sectiona4_detail'
    detail_url_name = 'sectiona5_detail'
    next_url_name = 'sectiona6_create'
    current_page = QAPP_PAGE_INDEX['section-a5']


class SectionA5Detail(SectionDetailBase):
    model = SectionA5
    section_title = SECTION_A['a5']['header']
    edit_url_name = 'sectiona5_edit'
    create_url_name = 'sectiona5_create'
    previous_url_name = 'sectiona4_detail'
    next_url_name = 'sectiona6_detail'
    current_page = QAPP_PAGE_INDEX['section-a5']


class SectionA6Create(SectionCreateBase):
    model = SectionA6
    form_class = forms.SectionA6Form
    section_title = SECTION_A['a6']['header']
    previous_url_name = 'sectiona5_detail'
    detail_url_name = 'sectiona6_detail'
    next_url_name = 'sectiona7_create'
    current_page = QAPP_PAGE_INDEX['section-a6']


class SectionA6Update(SectionUpdateBase):
    model = SectionA6
    form_class = forms.SectionA6Form
    section_title = SECTION_A['a6']['header']
    previous_url_name = 'sectiona5_detail'
    detail_url_name = 'sectiona6_detail'
    next_url_name = 'sectiona7_create'
    current_page = QAPP_PAGE_INDEX['section-a6']


class SectionA6Detail(SectionDetailBase):
    model = SectionA6
    section_title = SECTION_A['a6']['header']
    edit_url_name = 'sectiona6_edit'
    create_url_name = 'sectiona6_create'
    previous_url_name = 'sectiona5_detail'
    next_url_name = 'sectiona7_detail'
    current_page = QAPP_PAGE_INDEX['section-a6']


class SectionA7Detail(SectionTemplateView):

    template_name = 'qapp/sectiona/a7_detail.html'
    section_title = SECTION_A['a7']['header']
    edit_url_name = 'sectiona7_edit'
    create_url_name = 'sectiona7_create'
    previous_url_name = 'sectiona6_detail'
    next_url_name = 'sectiona8_detail'
    current_page = QAPP_PAGE_INDEX['section-a7']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.section_title
        context['previous_url'] = reverse(
            self.previous_url_name, kwargs={'qapp_id': self.kwargs['qapp_id']})
        context['next_url'] = reverse(
            self.next_url_name, kwargs={'qapp_id': self.kwargs['qapp_id']})
        context['distribution_list'] = Distribution.objects.filter(
            qapp_id=self.kwargs['qapp_id'])
        context['qapp_id'] = self.kwargs['qapp_id']

        return context


class SectionA8Detail(SectionTemplateView):

    template_name = 'qapp/sectiona/a8_detail.html'
    section_title = SECTION_A['a8']['header']
    edit_url_name = 'sectiona8_edit'
    create_url_name = 'sectiona8_create'
    previous_url_name = 'sectiona7_detail'
    next_url_name = 'sectiona9_detail'
    current_page = QAPP_PAGE_INDEX['section-a8']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.section_title
        context['previous_url'] = reverse(
            self.previous_url_name, kwargs={'qapp_id': self.kwargs['qapp_id']})
        context['next_url'] = reverse(
            self.next_url_name, kwargs={'qapp_id': self.kwargs['qapp_id']})
        context['roles_responsibilities'] = RoleResponsibility.objects.filter(
            qapp_id=self.kwargs['qapp_id'])
        context['qapp_id'] = self.kwargs['qapp_id']

        return context


# NOTE: Section A9 is readonly/boilerplate

class SectionA9Detail(SectionTemplateView):
    section_title = SECTION_A['a9']['header']
    previous_url_name = 'sectiona8_detail'
    next_url_name = 'sectiona10_detail'
    template_name = 'qapp/section_boilerplate.html'
    current_page = QAPP_PAGE_INDEX['section-a9']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qapp_id'] = self.kwargs['qapp_id']
        context['boilerplate'] = mark_safe(SECTION_A['a9']['boilerplate'])
        return context


class SectionA10Create(SectionCreateBase):
    model = SectionA10
    form_class = forms.SectionA10Form
    section_title = SECTION_A['a10']['header']
    previous_url_name = 'sectiona9_detail'
    detail_url_name = 'sectiona10_detail'
    next_url_name = 'sectiona11_create'
    boilerplate = SECTION_A['a10']['boilerplate']
    current_page = QAPP_PAGE_INDEX['section-a10']


class SectionA10Update(SectionUpdateBase):
    model = SectionA10
    form_class = forms.SectionA10Form
    section_title = SECTION_A['a10']['header']
    previous_url_name = 'sectiona9_detail'
    detail_url_name = 'sectiona10_detail'
    next_url_name = 'sectiona11_create'
    current_page = QAPP_PAGE_INDEX['section-a10']


class SectionA10Detail(SectionDetailBase):
    model = SectionA10
    section_title = SECTION_A['a10']['header']
    edit_url_name = 'sectiona10_edit'
    create_url_name = 'sectiona10_create'
    previous_url_name = 'sectiona9_detail'
    next_url_name = 'sectiona11_detail'
    current_page = QAPP_PAGE_INDEX['section-a10']


class SectionA11Create(SectionCreateBase):
    model = SectionA11
    form_class = forms.SectionA11Form
    section_title = SECTION_A['a11']['header']
    previous_url_name = 'sectiona10_detail'
    detail_url_name = 'sectiona11_detail'
    next_url_name = 'sectiona12_detail'
    current_page = QAPP_PAGE_INDEX['section-a11']


class SectionA11Update(SectionUpdateBase):
    model = SectionA11
    form_class = forms.SectionA11Form
    section_title = SECTION_A['a11']['header']
    previous_url_name = 'sectiona10_detail'
    detail_url_name = 'sectiona11_detail'
    next_url_name = 'sectiona12_detail'
    current_page = QAPP_PAGE_INDEX['section-a11']


class SectionA11Detail(SectionDetailBase):
    model = SectionA11
    section_title = SECTION_A['a11']['header']
    edit_url_name = 'sectiona11_edit'
    create_url_name = 'sectiona11_create'
    previous_url_name = 'sectiona10_detail'
    next_url_name = 'sectiona12_detail'
    current_page = QAPP_PAGE_INDEX['section-a11']


class SectionA12Detail(SectionTemplateView):

    template_name = 'qapp/sectiona/a12_detail.html'
    section_title = SECTION_A['a12']['header']
    create_url_name = 'sectiona12_detail'
    previous_url_name = 'sectiona11_detail'
    next_url_name = 'sectionb_detail'
    current_page = QAPP_PAGE_INDEX['section-a12']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.section_title
        context['previous_url'] = reverse(
            self.previous_url_name, kwargs={'qapp_id': self.kwargs['qapp_id']})
        context['next_url'] = reverse(
            self.next_url_name, kwargs={'qapp_id': self.kwargs['qapp_id']})
        # TODO: HERE
        context['distribution_list'] = Distribution.objects.filter(
            qapp_id=self.kwargs['qapp_id'])
        context['qapp_id'] = self.kwargs['qapp_id']
        context['documents_records'] = DocumentRecord.objects.filter(
            qapp_id=self.kwargs['qapp_id'])
        return context
