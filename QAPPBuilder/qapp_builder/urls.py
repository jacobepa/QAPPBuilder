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
from qapp_builder.settings import MEDIA_ROOT, MEDIA_URL

sections_a = [
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
    ('section-a8', section_a_views.SectionA8Create,
     section_a_views.SectionA8Update, section_a_views.SectionA8Detail),
    ('section-a11', section_a_views.SectionA11Create,
     section_a_views.SectionA11Update, section_a_views.SectionA11Detail),
    ('section-a12', section_a_views.SectionA12Create,
     section_a_views.SectionA12Update, section_a_views.SectionA12Detail),
]


urlpatterns = [
    path('admin', admin.site.urls),

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
         section_a_views.AdditionalSignatureCreate.as_view(),
         name='signature_create'),
    path('qapp/<int:qapp_id>/signature/<int:pk>/edit/',
         section_a_views.AdditionalSignatureUpdate.as_view(),
         name='signature_update'),
    path('qapp/<int:qapp_id>/signature/<int:pk>/delete/',
         section_a_views.AdditionalSignatureDelete.as_view(),
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
         section_a_views.AcronymAbbreviationCreate.as_view(),
         name='definition_create'),
    path('qapp/<int:qapp_id>/definition/<int:pk>/delete/',
         section_a_views.AcronymAbbreviationDelete.as_view(),
         name='definition_delete'),
    # Section A7 - ---------------- -----------------------------------
    path('qapp/<int:qapp_id>/section-a7/',
         section_a_views.SectionA7Detail.as_view(),
         name='sectiona7_detail'),
    path('qapp/<int:qapp_id>/section-a7/',
         section_a_views.SectionA7Detail.as_view(),
         name='sectiona7_create'),
    # Section A7 - Distribution List -----------------------------------
    # TODO
    # Section A9 and A10 -----------------------------------------------
    # are readonly and so only have a single URL each
    path('qapp/<int:qapp_id>/section-a9/',
         section_a_views.SectionA9Detail.as_view(),
         name='sectiona9_detail'),
    path('qapp/<int:qapp_id>/section-a10/',
         section_a_views.SectionA10Detail.as_view(),
         name='sectiona10_detail'),
    # ########################################################################
    # Section B URLs ---------------------------------------------------------
    # ########################################################################

    # Begin other module import URLs.
    path('accounts/', include('accounts.urls')),
    path('support/', include('support.urls')),
    path('teams/', include('teams.urls')),
]


# Loop through the sections to create URL patterns
for section, create_view, update_view, detail_view in sections_a:
    urlpatterns += [
        path(f'qapp/<int:qapp_id>/{section}/create/',
             create_view.as_view(), name=f'{section.replace("-", "")}_create'),
        path(f'qapp/<int:qapp_id>/{section}/edit/',
             update_view.as_view(), name=f'{section.replace("-", "")}_edit'),
        path(f'qapp/<int:qapp_id>/{section}/detail/',
             detail_view.as_view(), name=f'{section.replace("-", "")}_detail'),
    ]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
