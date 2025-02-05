from django.db import models


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
