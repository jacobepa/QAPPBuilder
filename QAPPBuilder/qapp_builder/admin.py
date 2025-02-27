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
from .models import SectionA1, SectionA2, SectionA4, SectionA5, SectionA6, \
    SectionA10, SectionA11, SectionB, SectionB7, SectionC, SectionD, \
    Qapp, Discipline, AdditionalSignature, Distribution, RoleResponsibility, \
    DocumentRecord


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
admin.site.register(SectionA1)
admin.site.register(SectionA2)
admin.site.register(SectionA4)
admin.site.register(SectionA5)
admin.site.register(SectionA6)
admin.site.register(SectionA10)
admin.site.register(SectionA11)
admin.site.register(SectionB)
admin.site.register(SectionB7)
admin.site.register(SectionC)
admin.site.register(SectionD)
admin.site.register(AdditionalSignature)
admin.site.register(Distribution)
admin.site.register(RoleResponsibility)
admin.site.register(DocumentRecord)
