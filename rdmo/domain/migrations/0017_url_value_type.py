# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-09 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0016_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='value_type',
            field=models.CharField(choices=[('text', 'Text'), ('url', 'URL'), ('integer', 'Integer'), ('float', 'Float'), ('boolean', 'Boolean'), ('datetime', 'Datetime'), ('options', 'Options')], max_length=8),
        ),
    ]
