# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-07 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professional_details', '0013_auto_20171105_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='awarded',
            field=models.IntegerField(verbose_name=b'Phd Awarded'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='industrial_exp',
            field=models.CharField(max_length=100, verbose_name=b'Industrial Experience'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='pursuing',
            field=models.IntegerField(verbose_name=b'Phd Pursuing'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='submitted',
            field=models.IntegerField(verbose_name=b'Phd Submitted'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b'Academic Experience'),
        ),
    ]