# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-07 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication_details', '0004_auto_20171107_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='page_no_end',
            field=models.IntegerField(default=21, verbose_name=b'Page number ending'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conference',
            name='page_no_start',
            field=models.IntegerField(default=21, verbose_name=b'Page number starting'),
            preserve_default=False,
        ),
    ]
