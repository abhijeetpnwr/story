# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-04 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='brief',
            field=models.CharField(default='story of sherlock holmes adventures to thrill you ', max_length=250),
            preserve_default=False,
        ),
    ]