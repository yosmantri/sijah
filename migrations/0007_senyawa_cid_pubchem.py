# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamu_app', '0006_penyakit_update_pada'),
    ]

    operations = [
        migrations.AddField(
            model_name='senyawa',
            name='CID_pubchem',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
