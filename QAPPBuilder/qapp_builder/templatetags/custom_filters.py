from django import template
from django.utils.safestring import mark_safe

register = template.Library()


def as_epa(field):
    return mark_safe(f'''
    <div class="usa-form-group">
        <label for="{field.id_for_label}" class="usa-label">
            {field.label}
        </label>
        {field}
        {field.errors}
    </div>
    ''')


register.filter('as_epa', as_epa)
