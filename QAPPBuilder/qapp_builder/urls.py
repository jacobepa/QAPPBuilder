# urls.py (qapp_builder)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov


"""Definition of urls for qapp_builder."""

from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
import qapp_builder.views.qapp_views as qapp_views
import qapp_builder.views.section_a_views as section_a_views
import qapp_builder.views.section_b_views as section_b_views
import qapp_builder.views.table_based_model_views as table_views
from qapp_builder.settings import MEDIA_ROOT, MEDIA_URL

sections_a_b = [
    ('section-a1', section_a_views.SectionA1Create,
     section_a_views.SectionA1Update, section_a_views.SectionA1Detail),
    ('section-a2', section_a_views.SectionA2Create,
     section_a_views.SectionA2Update, section_a_views.SectionA2Detail),
    ('section-a4', section_a_views.SectionA4Create,
     section_a_views.SectionA4Update, section_a_views.SectionA4Detail),
    ('section-a5', section_a_views.SectionA5Create,
     section_a_views.SectionA5Update, section_a_views.SectionA5Detail),
    ('section-a6', section_a_views.SectionA6Create,
     section_a_views.SectionA6Update, section_a_views.SectionA6Detail),
    ('section-a10', section_a_views.SectionA10Create,
     section_a_views.SectionA10Update, section_a_views.SectionA10Detail),
    ('section-a11', section_a_views.SectionA11Create,
     section_a_views.SectionA11Update, section_a_views.SectionA11Detail),
    ('section-b', section_b_views.SectionBCreate,
     section_b_views.SectionBUpdate, section_b_views.SectionBDetail),
    ('section-b7', section_b_views.SectionB7Create,
     section_b_views.SectionB7Update, section_b_views.SectionB7Detail),
]


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', qapp_views.QappIndex.as_view(), name='home'),
    path('dashboard/', qapp_views.QappIndex.as_view(), name='dashboard'),
    path('contact/', qapp_views.contact, name='contact'),

    path('dev/', qapp_views.web_dev_tools, name='web_dev_tools'),
    path('dev/clean_qapps/', qapp_views.clean_qapps, name='clean_qapps'),

    # ###################################################################
    # QAPP URLs ---------------------------------------------------------
    path('qapp/list/user/<int:user_id>/',
         qapp_views.QappList.as_view(),
         name='qapp_list_user'),
    path('qapp/list/team/<int:team_id>/',
         qapp_views.QappList.as_view(),
         name='qapp_list_team'),
    path('qapp/create/',
         qapp_views.QappCreateView.as_view(),
         name='qapp_create'),
    path('qapp/<int:pk>/detail/',
         qapp_views.QappDetail.as_view(),
         name='qapp_detail'),
    path('qapp/<int:qapp_id>/detail/',
         qapp_views.QappDetail.as_view(),
         name='qapp_detail'),
    path('qapp/<int:pk>/edit/',
         qapp_views.QappUpdate.as_view(),
         name='qapp_edit'),
    path('qapp/<int:qapp_id>/edit/',
         qapp_views.QappUpdate.as_view(),
         name='qapp_edit'),
    path('qapp/<int:pk>/delete/',
         qapp_views.QappDelete.as_view(),
         name='qapp_delete'),
    # QAPP Revisions ----------------------------------------------------
    path('qapp/<int:qapp_id>/revision/create/',
         qapp_views.RevisionCreate.as_view(),
         name='revision_edit'),
    path('qapp/<int:qapp_id>/revision/<int:pk>/edit/',
         qapp_views.RevisionUpdate.as_view(),
         name='revision_edit'),
    path('qapp/<int:qapp_id>/revision/<int:pk>/delete/',
         qapp_views.RevisionDelete.as_view(),
         name='revision_delete'),
    # ###################################################################
    # Section A URLs ----------------------------------------------------
    # Section A2 Signatures ---------------------------------------------
    path('qapp/<int:qapp_id>/signature/create/',
         table_views.AdditionalSignatureCreate.as_view(),
         name='signature_create'),
    path('qapp/<int:qapp_id>/signature/<int:pk>/edit/',
         table_views.AdditionalSignatureUpdate.as_view(),
         name='signature_edit'),
    path('qapp/<int:qapp_id>/signature/<int:pk>/delete/',
         table_views.AdditionalSignatureDelete.as_view(),
         name='signature_delete'),
    # Section A3  ------------------------------------------------------
    path('qapp/<int:qapp_id>/section-a3/',
         section_a_views.SectionA3Detail.as_view(),
         name='sectiona3_detail'),
    path('qapp/<int:qapp_id>/section-a3/',
         section_a_views.SectionA3Detail.as_view(),
         name='sectiona3_create'),
    # Section A3 Acronyms/Abbreviations --------------------------------
    path('qapp/<int:qapp_id>/definition/create/',
         table_views.AcronymAbbreviationCreate.as_view(),
         name='definition_create'),
    path('qapp/<int:qapp_id>/definition/<int:pk>/delete/',
         table_views.AcronymAbbreviationDelete.as_view(),
         name='definition_delete'),
    # Section A7 -------------------------------------------------------
    path('qapp/<int:qapp_id>/section-a7/',
         section_a_views.SectionA7Detail.as_view(),
         name='sectiona7_detail'),
    path('qapp/<int:qapp_id>/section-a7/',
         section_a_views.SectionA7Detail.as_view(),
         name='sectiona7_create'),
    # Section A7 - Distribution List -----------------------------------
    path('qapp/<int:qapp_id>/distribution/create/',
         table_views.DistributionCreate.as_view(),
         name='distribution_create'),
    path('qapp/<int:qapp_id>/distribution/<int:pk>/edit/',
         table_views.DistributionUpdate.as_view(),
         name='distribution_edit'),
    path('qapp/<int:qapp_id>/distribution/<int:pk>/delete/',
         table_views.DistributionDelete.as_view(),
         name='distribution_delete'),
    # Section A8 -------------------------------------------------------
    path('qapp/<int:qapp_id>/section-a8/',
         section_a_views.SectionA8Detail.as_view(),
         name='sectiona8_detail'),
    path('qapp/<int:qapp_id>/section-a8/',
         section_a_views.SectionA8Detail.as_view(),
         name='sectiona8_create'),
    # Section A8 - Project Organization --------------------------------
    path('qapp/<int:qapp_id>/role-responsibility/create/',
         table_views.RoleResponsibilityCreate.as_view(),
         name='role_responsibility_create'),
    path('qapp/<int:qapp_id>/role-responsibility/<int:pk>/edit/',
         table_views.RoleResponsibilityUpdate.as_view(),
         name='role_responsibility_edit'),
    path('qapp/<int:qapp_id>/role-responsibility/<int:pk>/delete/',
         table_views.RoleResponsibilityDelete.as_view(),
         name='role_responsibility_delete'),
    # Section A9 -------------------------------------------------------
    path('qapp/<int:qapp_id>/section-a9/',
         section_a_views.SectionA9Detail.as_view(),
         name='sectiona9_detail'),
    # Section A10 ------------------------------------------------------
    path('qapp/<int:qapp_id>/section-a10/',
         section_a_views.SectionA10Detail.as_view(),
         name='sectiona10_detail'),
    # Section A12 - Documents and Records ------------------------------
    path('qapp/<int:qapp_id>/section-a12/',
         section_a_views.SectionA12Detail.as_view(),
         name='sectiona12_detail'),
    # Documents and Records
    path('qapp/<int:qapp_id>/document-record/create/',
         table_views.DocumentRecordCreate.as_view(),
         name='document_record_create'),
    path('qapp/<int:qapp_id>/document-record/<int:pk>/edit/',
         table_views.DocumentRecordUpdate.as_view(),
         name='document_record_edit'),
    path('qapp/<int:qapp_id>/document-record/<int:pk>/delete/',
         table_views.DocumentRecordDelete.as_view(),
         name='document_record_delete'),
    # ########################################################################
    # Section B URLs ---------------------------------------------------------
    path('qapp/<int:qapp_id>/hardware-software/create/',
         table_views.HardwareSoftwareCreate.as_view(),
         name='hardware_software_create'),
    path('qapp/<int:qapp_id>/hardware-software/<int:pk>/edit/',
         table_views.HardwareSoftwareUpdate.as_view(),
         name='hardware_software_edit'),
    path('qapp/<int:qapp_id>/hardware-software/<int:pk>/delete/',
         table_views.HardwareSoftwareDelete.as_view(),
         name='hardware_software_delete'),
    # ########################################################################
    # Section C and D URLs ---------------------------------------------------
    path('qapp/<int:qapp_id>/section-c/',
         section_b_views.SectionB7Detail.as_view(),
         name='sectionc_detail'),
    # ########################################################################
    # Begin other module import URLs.
    path('accounts/', include('accounts.urls')),
    path('support/', include('support.urls')),
    path('teams/', include('teams.urls')),
]


# Loop through the sections to create URL patterns
for section, create_view, update_view, detail_view in sections_a_b:
    urlpatterns += [
        path(f'qapp/<int:qapp_id>/{section}/create/',
             create_view.as_view(), name=f'{section.replace("-", "")}_create'),
        path(f'qapp/<int:qapp_id>/{section}/edit/',
             update_view.as_view(), name=f'{section.replace("-", "")}_edit'),
        path(f'qapp/<int:qapp_id>/{section}/detail/',
             detail_view.as_view(), name=f'{section.replace("-", "")}_detail'),
    ]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
