# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-26 15:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0022_auto_20180726_1521'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Province',
        ),
    ]