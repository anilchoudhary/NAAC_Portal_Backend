# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-26 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects_taken', '0004_subjectstaken_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subjectstaken',
            old_name='subject',
            new_name='title',
        ),
    ]