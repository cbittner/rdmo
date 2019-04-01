# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-13 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0041_data_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='comment',
            field=models.TextField(blank=True, help_text='Additional internal information about this catalog.', verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='key',
            field=models.SlugField(blank=True, help_text='The internal identifier of this catalog.', max_length=128, verbose_name='Key'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='title_lang1',
            field=models.CharField(blank=True, help_text='The title for this catalog in the primary language.', max_length=256, verbose_name='Title (primary)'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='title_lang2',
            field=models.CharField(blank=True, help_text='The title for this catalog in the secondary language.', max_length=256, verbose_name='Title (secondary)'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='title_lang3',
            field=models.CharField(blank=True, help_text='The title for this catalog in the tertiary language.', max_length=256, verbose_name='Title (tertiary)'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='title_lang4',
            field=models.CharField(blank=True, help_text='The title for this catalog in the quaternary language.', max_length=256, verbose_name='Title (quaternary)'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='title_lang5',
            field=models.CharField(blank=True, help_text='The title for this catalog in the quinary language.', max_length=256, verbose_name='Title (quinary)'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='uri',
            field=models.URLField(blank=True, help_text='The Uniform Resource Identifier of this catalog (auto-generated).', max_length=640, verbose_name='URI'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='uri_prefix',
            field=models.URLField(blank=True, help_text='The prefix for the URI of this catalog.', max_length=256, verbose_name='URI Prefix'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='comment',
            field=models.TextField(blank=True, help_text='Additional internal information about this questionset.', verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='help_lang1',
            field=models.TextField(blank=True, help_text='The help text for this questionset in the primary language.', verbose_name='Help (primary)'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='help_lang2',
            field=models.TextField(blank=True, help_text='The help text for this questionset in the secondary language.', verbose_name='Help (secondary)'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='help_lang3',
            field=models.TextField(blank=True, help_text='The help text for this questionset in the tertiary language.', verbose_name='Help (tertiary)'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='help_lang4',
            field=models.TextField(blank=True, help_text='The help text for this questionset in the quaternary language.', verbose_name='Help (quaternary)'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='help_lang5',
            field=models.TextField(blank=True, help_text='The help text for this questionset in the quinary language.', verbose_name='Help (quinary)'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='key',
            field=models.SlugField(blank=True, help_text='The internal identifier of this questionset.', max_length=128, verbose_name='Key'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='path',
            field=models.CharField(blank=True, help_text='The path part of the URI of this questionset (auto-generated).', max_length=512, verbose_name='Path'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='title_lang1',
            field=models.CharField(blank=True, help_text='The title for this questionset in the primary language.', max_length=256, verbose_name='Title (primary)'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='title_lang2',
            field=models.CharField(blank=True, help_text='The title for this questionset in the secondary language.', max_length=256, verbose_name='Title (secondary)'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='title_lang3',
            field=models.CharField(blank=True, help_text='The title for this questionset in the tertiary language.', max_length=256, verbose_name='Title (tertiary)'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='title_lang4',
            field=models.CharField(blank=True, help_text='The title for this questionset in the quaternary language.', max_length=256, verbose_name='Title (quaternary)'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='title_lang5',
            field=models.CharField(blank=True, help_text='The title for this questionset in the quinary language.', max_length=256, verbose_name='Title (quinary)'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='uri',
            field=models.URLField(blank=True, help_text='The Uniform Resource Identifier of this questionset (auto-generated).', max_length=640, verbose_name='URI'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='uri_prefix',
            field=models.URLField(blank=True, help_text='The prefix for the URI of this questionset.', max_length=256, verbose_name='URI Prefix'),
        ),
        migrations.AlterField(
            model_name='section',
            name='comment',
            field=models.TextField(blank=True, help_text='Additional internal information about this section.', verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='section',
            name='key',
            field=models.SlugField(blank=True, help_text='The internal identifier of this section.', max_length=128, verbose_name='Key'),
        ),
        migrations.AlterField(
            model_name='section',
            name='path',
            field=models.CharField(blank=True, help_text='The path part of the URI of this section (auto-generated).', max_length=512, verbose_name='Label'),
        ),
        migrations.AlterField(
            model_name='section',
            name='title_lang1',
            field=models.CharField(blank=True, help_text='The title for this section in the primary language.', max_length=256, verbose_name='Title (primary)'),
        ),
        migrations.AlterField(
            model_name='section',
            name='title_lang2',
            field=models.CharField(blank=True, help_text='The title for this section in the secondary language.', max_length=256, verbose_name='Title (secondary)'),
        ),
        migrations.AlterField(
            model_name='section',
            name='title_lang3',
            field=models.CharField(blank=True, help_text='The title for this section in the tertiary language.', max_length=256, verbose_name='Title (tertiary)'),
        ),
        migrations.AlterField(
            model_name='section',
            name='title_lang4',
            field=models.CharField(blank=True, help_text='The title for this section in the quaternary language.', max_length=256, verbose_name='Title (quaternary)'),
        ),
        migrations.AlterField(
            model_name='section',
            name='title_lang5',
            field=models.CharField(blank=True, help_text='The title for this section in the quinary language.', max_length=256, verbose_name='Title (quinary)'),
        ),
        migrations.AlterField(
            model_name='section',
            name='uri',
            field=models.URLField(blank=True, help_text='The Uniform Resource Identifier of this section (auto-generated).', max_length=640, verbose_name='URI'),
        ),
        migrations.AlterField(
            model_name='section',
            name='uri_prefix',
            field=models.URLField(blank=True, help_text='The prefix for the URI of this section.', max_length=256, verbose_name='URI Prefix'),
        ),
    ]