# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-24 18:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoices',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
