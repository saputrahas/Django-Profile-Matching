# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-26 15:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0023_delete_province'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='karyawan',
            name='user',
        ),
    ]
