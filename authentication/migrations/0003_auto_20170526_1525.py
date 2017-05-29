# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-26 09:55
from __future__ import unicode_literals

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20170526_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=authentication.models.get_ProfileImage_path, verbose_name='profile image'),
        ),
    ]