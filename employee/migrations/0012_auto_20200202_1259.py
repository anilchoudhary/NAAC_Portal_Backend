# Generated by Django 3.0.2 on 2020-02-02 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0011_employee_csrf_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dontfill',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='employee_fs', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_allowed',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Phone'),
        ),
    ]
