# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-25 19:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects_taken', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subjectstaken',
            old_name='image',
            new_name='images',
        ),
    ]
