# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 18:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("query", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Query",
            new_name="Log",
        ),
    ]
