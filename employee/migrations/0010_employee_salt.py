# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-18 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_auto_20180131_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='salt',
            field=models.TextField(blank=True, null=True),
        ),
    ]
