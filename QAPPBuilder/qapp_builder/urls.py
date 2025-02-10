# urls.py (qapp_builder)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov


"""Definition of urls for qapp_builder."""

from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
import qapp_builder.views.views as views
import qapp_builder.views.section_a_views as section_a_views
from qapp_builder.settings import MEDIA_ROOT, MEDIA_URL


urlpatterns = [
  path('admin', admin.site.urls),

  path('', views.QappIndex.as_view(), name='home'),
  path('dashboard/', views.QappIndex.as_view(), name='dashboard'),
  path('contact/', views.contact, name='contact'),

  path('dev/', views.web_dev_tools, name='web_dev_tools'),
  path('dev/clean_qapps/', views.clean_qapps, name='clean_qapps'),

  # ###########################################################################
  # QAPP URLs ------------------------------------
  path('qapp/list/user/<int:pk>/',
       views.QappList.as_view(),
       name='qapp_list_user'),
  path('qapp/list/team/<int:pk>/',
       views.QappList.as_view(),
       name='qapp_list_team'),
  path('qapp/create/',
       views.QappCreateView.as_view(),
       name='qapp_create'),
  path('qapp/<int:pk>/detail/',
       views.QappDetail.as_view(),
       name='qapp_detail'),
  path('qapp/<int:pk>/edit/',
       views.QappUpdate.as_view(),
       name='qapp_update'),
  # SectionA URLs #############################################################
  # SectionA1 ------------------------------------
  path('qapp/<int:pk>/sectiona1/create/',
       section_a_views.SectionA1Create.as_view(),
       name='sectiona1_create'),
  path('qapp/<int:pk>/sectiona1/update/',
       section_a_views.SectionA1Update.as_view(),
       name='sectiona1_update'),
  path('qapp/<int:pk>/sectiona1/detail/',
       section_a_views.SectionA1Detail.as_view(),
       name='sectiona1_detail'),
  # SectionA2 ------------------------------------
  path('qapp/<int:pk>/sectiona2/create/',
       section_a_views.SectionA2Create.as_view(),
       name='sectiona2_create'),
  path('qapp/<int:pk>/sectiona2/update/',
       section_a_views.SectionA2Update.as_view(),
       name='sectiona2_update'),
  path('qapp/<int:pk>/sectiona2/detail/',
       section_a_views.SectionA2Detail.as_view(),
       name='sectiona2_detail'),
  # SectionA3 ------------------------------------
  # TODO....
  # SectionB URLs #############################################################
  # ###########################################################################

  # Begin other module import URLs.
  path('accounts/', include('accounts.urls')),
  path('support/', include('support.urls')),
  path('teams/', include('teams.urls')),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
