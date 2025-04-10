from django import template
from django.utils.safestring import mark_safe
from qapp_builder.models.utility_models import get_model_custom_label, \
    render_field

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


def render_detail(obj, field):
    return mark_safe(render_field(get_model_custom_label(obj, field),
                                  getattr(obj, field)))


register.filter('as_epa', as_epa)
register.filter('render_detail', render_detail)

@register.filter
def split(value, delimiter):
    """Split a string by a delimiter and return the list."""
    return value.split(delimiter)
