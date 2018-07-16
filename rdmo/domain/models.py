from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey

from rdmo.core.utils import get_uri_prefix
from rdmo.core.models import TranslationMixin

from .validators import AttributeEntityUniquePathValidator


@python_2_unicode_compatible
class AttributeEntity(MPTTModel):

    uri = models.URLField(
        max_length=640, blank=True, null=True,
        verbose_name=_('URI'),
        help_text=_('The Uniform Resource Identifier of this attribute/entity set (auto-generated).')
    )
    uri_prefix = models.URLField(
        max_length=256, blank=True, null=True,
        verbose_name=_('URI Prefix'),
        help_text=_('The prefix for the URI of this attribute/entity.')
    )
    key = models.SlugField(
        max_length=128, blank=True, null=True,
        verbose_name=_('Key'),
        help_text=_('The internal identifier of this attribute/entity.')
    )
    comment = models.TextField(
        blank=True, null=True,
        verbose_name=_('Comment'),
        help_text=_('Additional information about this attribute/entity.')
    )
    parent = TreeForeignKey(
        'self', null=True, blank=True, related_name='children', db_index=True,
        verbose_name=_('Parent entity'),
        help_text=_('Parent entity in the domain model.')
    )
    is_attribute = models.BooleanField(
        default=False,
        verbose_name=_('is attribute'),
        help_text=_('Designates whether this attribute/entity is an attribute (auto-generated).')
    )
    path = models.CharField(
        max_length=512, db_index=True,
        verbose_name=_('Path'),
        help_text=_('The path part of the URI of this attribute/entity (auto-generated).')
    )

    class Meta:
        ordering = ('uri', )
        verbose_name = _('Attribute entity')
        verbose_name_plural = _('Attribute entities')
        permissions = (('view_attributeentity', 'Can view Attribute entity'),)

    def __str__(self):
        return self.uri or self.key

    def save(self, *args, **kwargs):
        self.path = AttributeEntity.build_path(self.key, self.parent)
        self.uri = get_uri_prefix(self) + '/domain/' + self.path
        self.is_attribute = self.is_attribute or False

        super(AttributeEntity, self).save(*args, **kwargs)

        # recursively save children
        for child in self.children.all():
            child.save()

    def clean(self):
        self.path = AttributeEntity.build_path(self.key, self.parent)
        AttributeEntityUniquePathValidator(self)()

    @property
    def range(self):
        if self.is_attribute:
            return self.attribute.range
        else:
            return None

    @classmethod
    def build_path(self, key, parent):
        path = key
        while parent:
            path = parent.key + '/' + path
            parent = parent.parent
        return path


@python_2_unicode_compatible
class Attribute(AttributeEntity):

    class Meta:
        verbose_name = _('Attribute')
        verbose_name_plural = _('Attributes')
        permissions = (('view_attribute', 'Can view Attribute'),)

    def __str__(self):
        return self.uri or self.key

    def save(self, *args, **kwargs):
        self.is_attribute = True
        super(Attribute, self).save(*args, **kwargs)


@python_2_unicode_compatible
class VerboseName(models.Model, TranslationMixin):

    attribute_entity = models.OneToOneField(
        'AttributeEntity',
        verbose_name=_('Attribute entity'),
        help_text=_('Attribute/entity this verbose name belongs to.')
    )
    name_en = models.CharField(
        max_length=256,
        verbose_name=_('Name (en)'),
        help_text=_('English name displayed for this attribute/entity (e.g. project).')
    )
    name_de = models.CharField(
        max_length=256,
        verbose_name=_('Name (de)'),
        help_text=_('German name displayed for this attribute/entity (e.g. Projekt).')
    )
    name_plural_en = models.CharField(
        max_length=256,
        verbose_name=_('Plural name (en)'),
        help_text=_('English plural name displayed for this attribute/entity (e.g. projects).')
    )
    name_plural_de = models.CharField(
        max_length=256,
        verbose_name=_('Plural name (de)'),
        help_text=_('German plural name displayed for this attribute/entity (e.g. Projekte).')
    )

    class Meta:
        verbose_name = _('Verbose name')
        verbose_name_plural = _('Verbose names')
        permissions = (('view_verbosename', 'Can view Verbose name'),)

    def __str__(self):
        return self.attribute_entity.uri

    @property
    def name(self):
        return self.trans('name')

    @property
    def name_plural(self):
        return self.trans('name_plural')


@python_2_unicode_compatible
class Range(models.Model, TranslationMixin):

    attribute = models.OneToOneField(
        'Attribute',
        verbose_name=_('Attribute'),
        help_text=_('Attribute this verbose name belongs to.')
    )
    minimum = models.FloatField(
        verbose_name=_('Minimum'),
        help_text=_('Minimal value for this attribute.')
    )
    maximum = models.FloatField(
        verbose_name=_('Maximum'),
        help_text=_('Maximum value for this attribute.')
    )
    step = models.FloatField(
        verbose_name=_('Step'),
        help_text=_('Step in which this attribute can be incremented/decremented.')
    )

    class Meta:
        ordering = ('attribute', )
        verbose_name = _('Range')
        verbose_name_plural = _('Ranges')
        permissions = (('view_range', 'Can view Range'),)

    def __str__(self):
        return self.attribute.uri
