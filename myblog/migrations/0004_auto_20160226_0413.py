# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-26 04:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_auto_20160226_0358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'catagories'},
        ),
    ]
