# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-27 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20191224_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoices',
            name='comment',
            field=models.TextField(default='No comment', max_length=36, verbose_name='Comment'),
        ),
    ]
