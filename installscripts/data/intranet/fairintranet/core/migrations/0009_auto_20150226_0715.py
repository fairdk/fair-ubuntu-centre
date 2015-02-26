# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150224_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='icon_predefined',
            field=models.CharField(default='folder-open', max_length=64, verbose_name='default icon', choices=[('folder-open', 'folder-open'), ('video-camera', 'video-camera'), ('truck', 'truck'), ('rocket', 'rocket'), ('road', 'road'), ('question', 'question'), ('graduation-cap', 'graduation-cap'), ('globe', 'globe'), ('money', 'money'), ('desktop', 'desktop'), ('microphone', 'microphone'), ('code', 'code'), ('book', 'book'), ('comment', 'comment')]),
            preserve_default=True,
        ),
    ]
