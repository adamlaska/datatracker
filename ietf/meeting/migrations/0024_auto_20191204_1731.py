# Copyright The IETF Trust 2019-2020, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-04 17:31


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0023_create_scheduling_events'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='requested',
        ),
        migrations.RemoveField(
            model_name='session',
            name='requested_by',
        ),
        migrations.RemoveField(
            model_name='session',
            name='status',
        ),
    ]