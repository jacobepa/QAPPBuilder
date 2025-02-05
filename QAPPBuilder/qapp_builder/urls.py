# urls.py (qapp_builder)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov


"""Definition of urls for qapp_builder."""

from django.urls import re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from qapp_builder.views import QappIndex, contact, web_dev_tools, clean_qapps
from qapp_builder.settings import MEDIA_ROOT, MEDIA_URL


urlpatterns = [
  re_path(r'^admin', admin.site.urls),

  re_path(r'^$', QappIndex.as_view(), name='home'),
  re_path(r'^dashboard/?$', QappIndex.as_view(), name='dashboard'),
  re_path(r'^contact/?$', contact, name='contact'),

  re_path(r'^dev/?$', web_dev_tools, name='web_dev_tools'),
  re_path(r'^dev/clean_qapps/?$', clean_qapps, name='clean_qapps'),

  # Begin other module import URLs.
  re_path(r'^support/', include('support.urls')),
  re_path(r'^teams/', include('teams.urls')),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
