from django import forms
# from django.forms import modelformset_factory
from django.utils.safestring import mark_safe
# from django.contrib.admin.widgets import FilteredSelectMultiple


def as_epa(self_form):
  """
  Returns a provided form with EPA styling applied.
  Call this function from a ModelForm function defined as `def as_epa(self)`
  """
  output = []
  for field in self_form:
    output.append(render_field(self_form, field))
  return mark_safe('\n'.join(output))


def render_field(self_form, field):
  return f'''
  <div class="usa-form-group">
    <label for="{field.id_for_label}" class="usa-label">{field.label}</label>
    {field}
    {field.errors}
  </div>
  '''


def assign_epa_css(self_form):
  for field_name, field in self_form.fields.items():
    if not isinstance(field.widget, forms.SelectMultiple):
      field.widget.attrs['class'] = 'usa-input'
    else:
      field.widget.attrs['class'] = 'usa-select'
