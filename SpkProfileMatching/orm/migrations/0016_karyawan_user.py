# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-26 15:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orm', '0015_kecerdasan_karyawan'),
    ]

    operations = [
        migrations.AddField(
            model_name='karyawan',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
