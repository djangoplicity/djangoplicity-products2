# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-14 09:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products2', '0014_rbsejournal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mirror',
            options={'ordering': ['-priority', '-id'], 'verbose_name': 'The Mirror', 'verbose_name_plural': 'The Mirror'},
        ),
    ]
