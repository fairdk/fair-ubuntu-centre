# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_squashed_0004_auto_20150208_0455'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='icon_predefined',
            field=models.CharField(default=b'folder', max_length=64, verbose_name='default icon', choices=[(b'folder', b'folder'), (b'video-camera', b'video-camera'), (b'truck', b'truck'), (b'rocket', b'rocket'), (b'road', b'road'), (b'question', b'question'), (b'graduation-cap', b'graduation-cap')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ebook',
            name='resource_link',
            field=models.URLField(help_text='Find a book or movie file available on the intranet and copy the link here, e.g. http://localserver/path/to/book.pdf', verbose_name='resource link'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='resource_link',
            field=models.URLField(help_text='Find a book or movie file available on the intranet and copy the link here, e.g. http://localserver/path/to/book.pdf', verbose_name='resource link'),
            preserve_default=True,
        ),
    ]
