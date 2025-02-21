from django import template
from django.utils.safestring import mark_safe

register = template.Library()


def as_epa(field):
    error_str = ''
    if field.errors:
        error_str = f'<div class="usa-alert--error">{field.errors}</div>'
    return mark_safe(f'''
    <div class="usa-form-group">
        <label for="{field.id_for_label}" class="usa-label">
            {field.label}
        </label>
        {field}
        {error_str}
    </div>
    ''')


register.filter('as_epa', as_epa)
