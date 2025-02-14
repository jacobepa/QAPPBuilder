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
  path('qapp/<int:pk>/sectiona3/',
       section_a_views.SectionA3Page.as_view(),
       name='sectiona3_page'),
  # SectionA4 ------------------------------------
  path('qapp/<int:pk>/sectiona4/create/',
       section_a_views.SectionA4Create.as_view(),
       name='sectiona4_create'),
  path('qapp/<int:pk>/sectiona4/update/',
       section_a_views.SectionA4Update.as_view(),
       name='sectiona4_update'),
  path('qapp/<int:pk>/sectiona4/detail/',
       section_a_views.SectionA4Detail.as_view(),
       name='sectiona4_detail'),
#   # SectionA5 ------------------------------------
#   path('qapp/<int:pk>/sectiona5/create/',
#        section_a_views.SectionA5Create.as_view(),
#        name='sectiona5_create'),
#   path('qapp/<int:pk>/sectiona5/update/',
#        section_a_views.SectionA5Update.as_view(),
#        name='sectiona5_update'),
#   path('qapp/<int:pk>/sectiona5/detail/',
#        section_a_views.SectionA5Detail.as_view(),
#        name='sectiona5_detail'),
#   # SectionA6 ------------------------------------
#   path('qapp/<int:pk>/sectiona6/create/',
#        section_a_views.SectionA6Create.as_view(),
#        name='sectiona6_create'),
#   path('qapp/<int:pk>/sectiona6/update/',
#        section_a_views.SectionA6Update.as_view(),
#        name='sectiona6_update'),
#   path('qapp/<int:pk>/sectiona6/detail/',
#        section_a_views.SectionA6Detail.as_view(),
#        name='sectiona6_detail'),
#   # SectionA7 ------------------------------------
#   path('qapp/<int:pk>/sectiona7/create/',
#        section_a_views.SectionA7Create.as_view(),
#        name='sectiona7_create'),
#   path('qapp/<int:pk>/sectiona7/update/',
#        section_a_views.SectionA7Update.as_view(),
#        name='sectiona7_update'),
#   path('qapp/<int:pk>/sectiona7/detail/',
#        section_a_views.SectionA7Detail.as_view(),
#        name='sectiona7_detail'),
#   # SectionA8 ------------------------------------
#   path('qapp/<int:pk>/sectiona8/create/',
#        section_a_views.SectionA8Create.as_view(),
#        name='sectiona8_create'),
#   path('qapp/<int:pk>/sectiona8/update/',
#        section_a_views.SectionA8Update.as_view(),
#        name='sectiona8_update'),
#   path('qapp/<int:pk>/sectiona8/detail/',
#        section_a_views.SectionA8Detail.as_view(),
#        name='sectiona8_detail'),
#   # SectionA9 ------------------------------------
#   path('qapp/<int:pk>/sectiona9/create/',
#        section_a_views.SectionA9Create.as_view(),
#        name='sectiona9_create'),
#   path('qapp/<int:pk>/sectiona9/update/',
#        section_a_views.SectionA9Update.as_view(),
#        name='sectiona9_update'),
#   path('qapp/<int:pk>/sectiona9/detail/',
#        section_a_views.SectionA9Detail.as_view(),
#        name='sectiona9_detail'),
#   # SectionA10 ------------------------------------
#   path('qapp/<int:pk>/sectiona10/create/',
#        section_a_views.SectionA10Create.as_view(),
#        name='sectiona10_create'),
#   path('qapp/<int:pk>/sectiona10/update/',
#        section_a_views.SectionA10Update.as_view(),
#        name='sectiona10_update'),
#   path('qapp/<int:pk>/sectiona10/detail/',
#        section_a_views.SectionA10Detail.as_view(),
#        name='sectiona10_detail'),
#   # SectionA11 ------------------------------------
#   path('qapp/<int:pk>/sectiona11/create/',
#        section_a_views.SectionA11Create.as_view(),
#        name='sectiona11_create'),
#   path('qapp/<int:pk>/sectiona11/update/',
#        section_a_views.SectionA11Update.as_view(),
#        name='sectiona11_update'),
#   path('qapp/<int:pk>/sectiona11/detail/',
#        section_a_views.SectionA11Detail.as_view(),
#        name='sectiona11_detail'),
#   # SectionA12 ------------------------------------
#   path('qapp/<int:pk>/sectiona12/create/',
#        section_a_views.SectionA12Create.as_view(),
#        name='sectiona12_create'),
#   path('qapp/<int:pk>/sectiona12/update/',
#        section_a_views.SectionA12Update.as_view(),
#        name='sectiona12_update'),
#   path('qapp/<int:pk>/sectiona12/detail/',
#        section_a_views.SectionA12Detail.as_view(),
#        name='sectiona12_detail'),

  # TODO....
  # SectionB URLs #############################################################
  # ###########################################################################

  # Begin other module import URLs.
  path('accounts/', include('accounts.urls')),
  path('support/', include('support.urls')),
  path('teams/', include('teams.urls')),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
