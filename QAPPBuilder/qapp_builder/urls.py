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


urlpatterns = [
    path('admin', admin.site.urls),

    path('', qapp_views.QappIndex.as_view(), name='home'),
    path('dashboard/', qapp_views.QappIndex.as_view(), name='dashboard'),
    path('contact/', qapp_views.contact, name='contact'),

    path('dev/', qapp_views.web_dev_tools, name='web_dev_tools'),
    path('dev/clean_qapps/', qapp_views.clean_qapps, name='clean_qapps'),

    # ########################################################################
    # QAPP URLs --------------------------------------------------------------
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
    path('qapp/<int:pk>/edit/',
         qapp_views.QappUpdate.as_view(),
         name='qapp_edit'),
    # ########################################################################
    # Section A URLs ---------------------------------------------------------
    # --- Section A1 ---------------------------------------------------------
    path('qapp/<int:pk>/section-a1/create/',
         section_a_views.SectionA1Create.as_view(),
         name='sectiona1_create'),
    path('qapp/<int:pk>/section-a1/detail/',
         section_a_views.SectionA1Detail.as_view(),
         name='sectiona1_detail'),
    # --- Section A2 ---------------------------------------------------------
    path('qapp/<int:pk>/section-a2/create/',
         section_a_views.SectionA2Create.as_view(),
         name='sectiona2_create'),
    # --- Section A3 ---------------------------------------------------------
    # --- Section A4 ---------------------------------------------------------
    # --- Section A5 ---------------------------------------------------------
    # --- Section A6 ---------------------------------------------------------
    # ########################################################################
    # Section B URLs ---------------------------------------------------------
    # ########################################################################

    # Begin other module import URLs.
    path('accounts/', include('accounts.urls')),
    path('support/', include('support.urls')),
    path('teams/', include('teams.urls')),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
