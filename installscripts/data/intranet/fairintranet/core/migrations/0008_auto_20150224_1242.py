# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_externalcollection_resource_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='menu_order',
            field=models.PositiveSmallIntegerField(default=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='collection',
            name='icon_predefined',
            field=models.CharField(default='folder-open', max_length=64, verbose_name='default icon', choices=[('folder-open', 'folder-open'), ('video-camera', 'video-camera'), ('truck', 'truck'), ('rocket', 'rocket'), ('road', 'road'), ('question', 'question'), ('graduation-cap', 'graduation-cap'), ('globe', 'globe'), ('money', 'money'), ('desktop', 'desktop'), ('microphone', 'microphone'), ('code', 'code')]),
            preserve_default=True,
        ),
    ]
