# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-26 15:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0021_auto_20180726_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='karyawan',
            name='province',
        ),
        migrations.RemoveField(
            model_name='kecerdasan',
            name='karyawan',
        ),
        migrations.AddField(
            model_name='karyawan',
            name='kecerdasan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='karyawans', to='orm.Kecerdasan'),
        ),
    ]
