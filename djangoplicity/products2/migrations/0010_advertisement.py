# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-05 18:57
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import djangoplicity.archives.base
import djangoplicity.archives.fields
import djangoplicity.metadata.archives.fields
import djangoplicity.products2.base.consts


class Migration(migrations.Migration):

    dependencies = [
        ('products2', '0009_auto_20200915_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', djangoplicity.archives.fields.IdField(help_text='Ids are only allowed to contain letters, numbers, underscores or hyphens. They are used in URLs for the archive item.', primary_key=True, serialize=False)),
                ('title', djangoplicity.archives.fields.TitleField(db_index=True, help_text='Title is shown in browser window. Use a good informative title, since search engines normally display the title on their result pages.', max_length=200)),
                ('description', djangoplicity.archives.fields.DescriptionField(blank=True, help_text='')),
                ('priority', djangoplicity.archives.fields.PriorityField(db_index=True, default=0, help_text='Priority of product (100 highest, 0 lowest) - high priority products are ranked higher in search results than low priority products.')),
                ('credit', djangoplicity.metadata.archives.fields.AVMCreditField(blank=True, default=djangoplicity.products2.base.consts.DEFAULT_CREDIT_FUNC, help_text='The minimum information that the Publisher would like to see mentioned when the resource is used.', null=False)),
                ('width', models.CharField(blank=True, help_text='(cm)', max_length=10)),
                ('height', models.CharField(blank=True, help_text='(cm)', max_length=10)),
                ('depth', models.CharField(blank=True, help_text='(cm)', max_length=10)),
                ('weight', models.CharField(blank=True, default=0, help_text='(g)', max_length=10)),
                ('pages', models.PositiveSmallIntegerField(blank=True, help_text='Number of pages', null=True)),
                ('cover', models.CharField(blank=True, choices=[(b'Hardcover', b'Hardcover'), (b'Softcover', b'Softcover')], help_text='Type of cover', max_length=9)),
                ('language', models.CharField(blank=True, choices=[(b'ab', b'Abkhaz'), (b'aa', b'Afar'), (b'af', b'Afrikaans'), (b'ak', b'Akan'), (b'sq', b'Albanian'), (b'am', b'Amharic'), (b'ar', b'Arabic'), (b'an', b'Aragonese'), (b'hy', b'Armenian'), (b'as', b'Assamese'), (b'av', b'Avaric'), (b'ae', b'Avestan'), (b'ay', b'Aymara'), (b'az', b'Azerbaijani'), (b'bm', b'Bambara'), (b'ba', b'Bashkir'), (b'eu', b'Basque'), (b'be', b'Belarusian'), (b'bn', b'Bengali'), (b'bh', b'Bihari'), (b'bi', b'Bislama'), (b'bs', b'Bosnian'), (b'br', b'Breton'), (b'bg', b'Bulgarian'), (b'my', b'Burmese'), (b'ca', b'Catalan'), (b'ch', b'Chamorro'), (b'ce', b'Chechen'), (b'ny', b'Chichewa'), (b'zh', b'Chinese'), (b'cv', b'Chuvash'), (b'kw', b'Cornish'), (b'co', b'Corsican'), (b'cr', b'Cree'), (b'hr', b'Croatian'), (b'cs', b'Czech'), (b'da', b'Danish'), (b'dv', b'Divehi'), (b'nl', b'Dutch'), (b'dz', b'Dzongkha'), (b'en', b'English'), (b'et', b'Estonian'), (b'ee', b'Ewe'), (b'fo', b'Faroese'), (b'fj', b'Fijian'), (b'fi', b'Finnish'), (b'fr', b'French'), (b'ff', b'Fula'), (b'gl', b'Galician'), (b'ka', b'Georgian'), (b'de', b'German'), (b'el', b'Greek'), (b'kl', b'Greenlandic'), (b'gn', b'Guarani'), (b'gu', b'Gujarati'), (b'ht', b'Haitian'), (b'ha', b'Hausa'), (b'he', b'Hebrew'), (b'hz', b'Herero'), (b'hi', b'Hindi'), (b'ho', b'Hiri Motu'), (b'hu', b'Hungarian'), (b'is', b'Icelandic'), (b'ig', b'Igbo'), (b'id', b'Indonesian'), (b'iu', b'Inuktitut'), (b'ik', b'Inupiaq'), (b'ga', b'Irish'), (b'it', b'Italian'), (b'ja', b'Japanese'), (b'jv', b'Javanese'), (b'kn', b'Kannada'), (b'kr', b'Kanuri'), (b'ks', b'Kashmiri'), (b'kk', b'Kazakh'), (b'km', b'Khmer'), (b'ki', b'Kikuyu'), (b'rw', b'Kinyarwanda'), (b'ky', b'Kirghiz'), (b'rn', b'Kirundi'), (b'kv', b'Komi'), (b'kg', b'Kongo'), (b'ko', b'Korean'), (b'ku', b'Kurdish'), (b'kj', b'Kwanyama'), (b'lo', b'Lao'), (b'la', b'Latin'), (b'lv', b'Latvian'), (b'li', b'Limburgish'), (b'ln', b'Lingala'), (b'lt', b'Lithuanian'), (b'lu', b'Luba-Katanga'), (b'lg', b'Luganda'), (b'lb', b'Luxembourgish'), (b'mk', b'Macedonian'), (b'mg', b'Malagasy'), (b'ms', b'Malay'), (b'ml', b'Malayalam'), (b'mt', b'Maltese'), (b'gv', b'Manx'), (b'mi', b'Maori'), (b'mr', b'Marathi'), (b'mh', b'Marshallese'), (b'mn', b'Mongolian'), (b'na', b'Nauru'), (b'nv', b'Navajo'), (b'ng', b'Ndonga'), (b'ne', b'Nepali'), (b'nd', b'North Ndebele'), (b'se', b'Northern Sami'), (b'no', b'Norwegian'), (b'nb', b'Norwegian Bokm\xef\xbf\xbdl'), (b'nn', b'Norwegian Nynorsk'), (b'ii', b'Nuosu'), (b'oc', b'Occitan'), (b'oj', b'Ojibwe'), (b'or', b'Oriya'), (b'om', b'Oromo'), (b'os', b'Ossetian'), (b'pi', b'Pali'), (b'pa', b'Panjabi'), (b'ps', b'Pashto'), (b'fa', b'Persian'), (b'pl', b'Polish'), (b'pt', b'Portuguese'), (b'qu', b'Quechua'), (b'ro', b'Romanian'), (b'rm', b'Romansh'), (b'ru', b'Russian'), (b'sm', b'Samoan'), (b'sg', b'Sango'), (b'sa', b'Sanskrit'), (b'sc', b'Sardinian'), (b'gd', b'Scottish Gaelic'), (b'sr', b'Serbian'), (b'sr-latn', b'Serbian Latin'), (b'sn', b'Shona'), (b'sd', b'Sindhi'), (b'si', b'Sinhala'), (b'sk', b'Slovak'), (b'sl', b'Slovene'), (b'so', b'Somali'), (b'nr', b'South Ndebele'), (b'st', b'Southern Sotho'), (b'es', b'Spanish'), (b'su', b'Sundanese'), (b'sw', b'Swahili'), (b'ss', b'Swati'), (b'sv', b'Swedish'), (b'tl', b'Tagalog'), (b'ty', b'Tahitian'), (b'tg', b'Tajik'), (b'ta', b'Tamil'), (b'tt', b'Tatar'), (b'te', b'Telugu'), (b'th', b'Thai'), (b'bo', b'Tibetan Standard'), (b'ti', b'Tigrinya'), (b'to', b'Tonga'), (b'ts', b'Tsonga'), (b'tn', b'Tswana'), (b'tr', b'Turkish'), (b'tk', b'Turkmen'), (b'tw', b'Twi'), (b'ug', b'Uighur'), (b'uk', b'Ukrainian'), (b'ur', b'Urdu'), (b'uz', b'Uzbek'), (b've', b'Venda'), (b'vi', b'Vietnamese'), (b'wa', b'Walloon'), (b'cy', b'Welsh'), (b'fy', b'Western Frisian'), (b'wo', b'Wolof'), (b'xh', b'Xhosa'), (b'yi', b'Yiddish'), (b'yo', b'Yoruba'), (b'za', b'Zhuang'), (b'zu', b'Zulu')], max_length=2)),
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
                'verbose_name': 'Advertisement',
            },
            bases=(djangoplicity.archives.base.ArchiveModel, models.Model),
        ),
    ]
