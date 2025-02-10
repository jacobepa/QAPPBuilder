from django.db import models
from django.utils.dateformat import format as date_format
from django.utils.safestring import mark_safe
from qapp_builder.settings import DATETIME_FORMAT


class Definition(models.Model):
  """Represents a Definition for an Acronym, Abbreviation, or Term"""
  acronym_abbrev = models.TextField(blank=False, null=False)
  definition = models.TextField(blank=False, null=False)


class VersionControl(models.Model):
  """Represents a row in the version control table"""
  qapp_id = models.TextField(blank=False, null=False)
  updated_on = models.DateField(blank=False, null=False)
  authors = models.TextField(blank=False, null=False)
  description = models.TextField(blank=False, null=False)


class Participant(models.Model):
  """Represents an entry in the distribution list"""

  name_and_org = models.TextField()
  email = models.TextField()
  roles = models.TextField()
  responsibilities = models.TextField()


class QappDocument(models.Model):
  """
  Represents a Document or Record. SectionA12 will contain a table
  (i.e. many-to-many relationship) of documents/records.
  """
  record_type = models.TextField()
  responsible_party = models.TextField()
  location_proj_file = models.TextField()
  file_format = models.TextField()
  # TODO: Special handling should be Y or N
  special_handling = models.TextField()


def render_model_details(instance):
  """
  Returns the details of a model instance with USWDS styling.
  """
  output = []
  for field in instance._meta.fields:
    value = getattr(instance, field.name)
    if field.many_to_many:
      value = ', '.join([str(obj) for obj in value.all()])
    # TODO Figure out datetime formatting...
    # elif isinstance(value, (models.DateField, models.DateTimeField)):
    #   value = date_format(value, DATETIME_FORMAT)
    output.append(render_field(field.verbose_name.capitalize(), value))
  return mark_safe('\n'.join(output))


def render_field(label, value):
  return f'''
  <div class="usa-form-group">
    <label class="usa-label">{label}</label>
    <div class="usa-input">{value}</div>
  </div>
  '''
