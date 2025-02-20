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

    # Begin other module import URLs.
    path('accounts/', include('accounts.urls')),
    path('support/', include('support.urls')),
    path('teams/', include('teams.urls')),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
