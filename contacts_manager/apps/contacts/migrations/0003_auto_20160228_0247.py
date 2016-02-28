# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 02:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20160228_0243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinfo',
            name='person',
        ),
        migrations.AddField(
            model_name='person',
            name='contact_info',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.ContactInfo'),
        ),
    ]
