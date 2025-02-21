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
    path('qapp/list/user/<int:pk>/',
         qapp_views.QappList.as_view(),
         name='qapp_list'),
    path('qapp/list/team/<int:pk>/',
         qapp_views.QappList.as_view(),
         name='qapp_list'),
    path('qapp/create/',
         qapp_views.QappCreateView.as_view(),
         name='qapp_create'),
    path('qapp/<int:pk>/detail/',
         qapp_views.QappDetail.as_view(),
         name='qapp_detail'),
    # Section A URLs ---------------------------------------------------------
    path('qapp/<int:pk>/section-a/create/',
         section_a_views.SectionA1Create.as_view(),
         name='sectiona1_create'),
    # Section B URLs ---------------------------------------------------------
    # ########################################################################

    # Begin other module import URLs.
    path('accounts/', include('accounts.urls')),
    path('support/', include('support.urls')),
    path('teams/', include('teams.urls')),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
