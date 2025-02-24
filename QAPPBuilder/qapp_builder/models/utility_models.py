from django.db import models
from django.utils.safestring import mark_safe


class EpaBaseModel(models.Model):
    """Abstract class to be inherited by all EPA/QAPP Models."""

    def render_details(self):
        return render_model_details(self)

    class Meta:
        abstract = True


class Definition(EpaBaseModel):
    """Represents a Definition for an Acronym, Abbreviation, or Term"""

    acronym_abbrev = models.TextField(blank=False, null=False)
    definition = models.TextField(blank=False, null=False)


class Participant(EpaBaseModel):
    """Represents an entry in the distribution list (TODO what section?)"""

    name_and_org = models.TextField()
    email = models.TextField()
    roles = models.TextField()
    responsibilities = models.TextField()


class QappDocument(EpaBaseModel):
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


def render_field(label, value):
    return f'''
    <div class="usa-form-group">
        <label class="usa-label">{label}</label>
        <div class="usa-input">{value}</div>
    </div>
    '''


def get_model_custom_label(instance, field_name):
    # NOTE: Custom code for handling labels in the model rendering
    if hasattr(instance, 'labels') and field_name in instance.labels:
        return instance.labels[field_name]


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
        #     value = date_format(value, DATETIME_FORMAT)
        field_label = get_model_custom_label(instance, field.name)
        if not field_label:
            field_label = field.verbose_name.capitalize()
        output.append(render_field(field_label, value))
    return mark_safe('\n'.join(output))
