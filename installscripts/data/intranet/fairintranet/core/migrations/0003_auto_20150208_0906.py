# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150208_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='ebook',
            name='short_description',
            field=models.CharField(max_length=512, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.CharField(max_length=64, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='short_description',
            field=models.CharField(max_length=512, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='collection',
            name='icon_predefined',
            field=models.CharField(default=b'folder-open', max_length=64, verbose_name='default icon', choices=[(b'folder-open', b'folder-open'), (b'video-camera', b'video-camera'), (b'truck', b'truck'), (b'rocket', b'rocket'), (b'road', b'road'), (b'question', b'question'), (b'graduation-cap', b'graduation-cap')]),
            preserve_default=True,
        ),
    ]
