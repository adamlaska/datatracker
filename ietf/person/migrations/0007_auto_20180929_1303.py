# Copyright The IETF Trust 2018-2020, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-29 13:03


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0006_auto_20180910_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personevent',
            name='type',
            field=models.CharField(choices=[('apikey_login', 'API key login'), ('gdpr_notice_email', 'GDPR consent request email sent'), ('email_address_deactivated', 'Email address deactivated')], max_length=50),
        ),
    ]