# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-03-28 20:47
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import djangoplicity.archives.base
import djangoplicity.archives.fields
import djangoplicity.metadata.archives.fields
import djangoplicity.products2.base.consts


class Migration(migrations.Migration):

    dependencies = [
        ('products2', '0016_auto_20230322_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', djangoplicity.archives.fields.IdField(help_text='Ids are only allowed to contain letters, numbers, underscores or hyphens. They are used in URLs for the archive item.', primary_key=True, serialize=False)),
                ('title', djangoplicity.archives.fields.TitleField(db_index=True, help_text='Title is shown in browser window. Use a good informative title, since search engines normally display the title on their result pages.', max_length=200)),
                ('description', djangoplicity.archives.fields.DescriptionField(blank=True, help_text='')),
                ('priority', djangoplicity.archives.fields.PriorityField(db_index=True, default=0, help_text='Priority of product (100 highest, 0 lowest) - high priority products are ranked higher in search results than low priority products.')),
                ('credit', djangoplicity.metadata.archives.fields.AVMCreditField(blank=True, default=djangoplicity.products2.base.consts.DEFAULT_CREDIT_FUNC, help_text='The minimum information that the Publisher would like to see mentioned when the resource is used.', null=False)),
                ('file_duration', djangoplicity.metadata.archives.fields.AVMFileDuration(blank=True, help_text='The duration of the file in the format hh:mm:ss:frames.', max_length=13, null=True, verbose_name='File Duration')),
                ('release_date', djangoplicity.archives.fields.ReleaseDateTimeField(blank=True, db_index=True, null=True)),
                ('embargo_date', djangoplicity.archives.fields.ReleaseDateTimeField(blank=True, db_index=True, null=True)),
                ('published', models.BooleanField(db_index=True, default=False, verbose_name='Published')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last modified')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('release_task_id', models.CharField(blank=True, max_length=64, null=True)),
                ('embargo_task_id', models.CharField(blank=True, max_length=64, null=True)),
                ('checksums', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('archive_category', models.ManyToManyField(blank=True, to='products2.ArchiveCategory')),
            ],
            options={
                'ordering': ['-priority', '-id'],
                'abstract': False,
                'verbose_name': 'Podcast',
                'verbose_name_plural': 'Podcasts',
            },
            bases=(djangoplicity.archives.base.ArchiveModel, models.Model),
        ),
    ]
