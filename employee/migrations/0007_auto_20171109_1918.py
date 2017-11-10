# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-09 19:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_dontfill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dontfill',
            name='id',
        ),
        migrations.AlterField(
            model_name='dontfill',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='employee_fs', serialize=False, to='employee.Employee'),
        ),
    ]