# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_resourceusage_external_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='externalcollection',
            name='resource_link',
            field=models.CharField(default='123', help_text='Find a book or movie file available on the intranet and copy the link here, e.g. http://localserver/path/to/book.pdf', max_length=512, verbose_name='resource link'),
            preserve_default=False,
        ),
    ]
