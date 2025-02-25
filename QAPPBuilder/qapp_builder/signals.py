from django.db.models.signals import post_save
from django.dispatch import receiver
from qapp_builder.models import Qapp, Distribution, RoleResponsibility
from constants.qapp_section_a_const import DISTRIBUTION_LIST_DEFAULT_ROLES, \
    PROJ_ROLES_RESPONSIBILITIES


@receiver(post_save, sender=Qapp)
def create_divisions(sender, instance, created, **kwargs):
    if created:
        for key in DISTRIBUTION_LIST_DEFAULT_ROLES.keys():
            kwargs = {
                'qapp_id': instance.id,
                'name': '[UPDATE THIS]',
                'org': '[UPDATE THIS]',
                'email': '[UPDATE THIS]',
                'proj_role': key,
            }
            Distribution.objects.create(**kwargs)

        for key, value in PROJ_ROLES_RESPONSIBILITIES.items():
            kwargs = {
                'qapp_id': instance.id,
                'name': '[UPDATE THIS]',
                'org': '[UPDATE THIS]',
                'proj_role': key,
                # Responsibilities/values looks like ['resp 1', 'resp 2', ...]
                'proj_responsibilities': '\n'.join(value)
            }
            RoleResponsibility.objects.create(**kwargs)
