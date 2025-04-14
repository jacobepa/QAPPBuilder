from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _

IGNORE_FIELDS_PROGRESS = ['id']


class EpaBaseModel(models.Model):
    """Base model for EPA QAPP Builder models."""
    history = HistoricalRecords(inherit=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def render_details(self):
        return render_model_details(self)

    def get_progress(self):
        total_fields = 0
        empty_fields = 0
        for field in self._meta.get_fields():
            if (
                isinstance(field,
                           (models.ForeignKey, models.OneToOneField,
                            models.ManyToManyRel, models.ManyToOneRel,
                            models.AutoField)) or
                field.name in IGNORE_FIELDS_PROGRESS or
                getattr(field, 'null', True) or getattr(field, 'blank', True)
            ):
                continue

            total_fields += 1
            value = getattr(self, field.name, None)
            if value in [None, '', []]:  # Check for empty or null values
                empty_fields += 1

        if empty_fields == 0:
            return 100

        if total_fields == 0:
            return 0  # Avoid division by zero

        progress = (total_fields - empty_fields) / total_fields * 100
        return progress

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
    extra_class = 'long-text'
    if len(str(value)) > 100:
        extra_class = 'long-text-12'
    return f'''
    <div class="usa-form-group"
         role="group"
         aria-labelledby="field-label-{label}">
        <label class="usa-label" id="field-label-{label}">{label}</label>
        <div class="usa-input {extra_class}"
             role="textbox"
             aria-readonly="true"
             aria-label="{label}">{value}</div>
    </div>
    '''


def get_model_custom_label(instance, field_name):
    # NOTE: Custom code for handling labels in the model rendering
    if hasattr(instance, 'labels') and field_name in instance.labels:
        return instance.labels[field_name]


def render_model_details(self):
    """Render model details in a semantic and accessible way."""
    fields = []
    for field in self._meta.fields:
        if field.name not in ['id', 'created_at', 'updated_at']:
            label = get_model_custom_label(self, field.name)
            value = getattr(self, field.name)
            if value:
                fields.append(render_field(label, value))

    return f'''
    <section class="usa-section"
             role="region"
             aria-label="Model Details">
        <div class="usa-container">
            <h2 class="usa-heading"
                id="model-details-heading">
                {self._meta.verbose_name}
            </h2>
            <div class="usa-grid" role="list">
                {''.join(fields)}
            </div>
        </div>
    </section>
    '''
