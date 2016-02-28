# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20160228_0247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='contact_info',
        ),
        migrations.AddField(
            model_name='person',
            name='city',
            field=models.CharField(default='Brooklyn', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='country',
            field=models.CharField(default='US', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='email_address',
            field=models.CharField(default='ericfries@gmail.com', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='phone_number',
            field=models.CharField(default='917.224.3534', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='postal_code',
            field=models.CharField(default='11249', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='state',
            field=models.CharField(default='NY', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='street_address_1',
            field=models.CharField(default='148 N. 9th Street', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='street_address_2',
            field=models.CharField(default='#1L', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ContactInfo',
        ),
    ]