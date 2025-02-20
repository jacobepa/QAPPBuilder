# admin.py (qapp_builder)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov


"""
Defines classes used to generate Django Admin portion of website.

Should be an Admin class for each Model that can be modified by an admin user.

Available functions:
- TBD
"""

from django.contrib import admin
from .models import Qapp, Discipline


class QappAdmin(admin.ModelAdmin):
    """
    Define options used to display and edit Qapp objects.

    (qapp_builder) on the Django Admin page.
    """

    def save_model(self, request, obj, form, change):
        """
        Overwrite the default save_model method.

        So we can automatically set the created_by field as current user.
        """
        # Only set created_by when it's the first save (create)
        if not obj.pk:
            obj.created_by = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Qapp, QappAdmin)
admin.site.register(Discipline)
