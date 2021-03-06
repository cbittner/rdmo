# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-05 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('options', '0016_meta'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='text_lang3',
            field=models.CharField(blank=True, help_text='The text for this option in the tertiary language.', max_length=256, null=True, verbose_name='Text (tertiary)'),
        ),
        migrations.AddField(
            model_name='option',
            name='text_lang4',
            field=models.CharField(blank=True, help_text='The text for this option in the quaternary language.', max_length=256, null=True, verbose_name='Text (quaternary)'),
        ),
        migrations.AddField(
            model_name='option',
            name='text_lang5',
            field=models.CharField(blank=True, help_text='The text for this option in the quinary language.', max_length=256, null=True, verbose_name='Text (quinary)'),
        ),
        migrations.AlterField(
            model_name='option',
            name='text_lang1',
            field=models.CharField(blank=True, help_text='The text for this option in the primary language.', max_length=256, null=True, verbose_name='Text (primary)'),
        ),
        migrations.AlterField(
            model_name='option',
            name='text_lang2',
            field=models.CharField(blank=True, help_text='The text for this option in the secondary language.', max_length=256, null=True, verbose_name='Text (secondary)'),
        ),
    ]
