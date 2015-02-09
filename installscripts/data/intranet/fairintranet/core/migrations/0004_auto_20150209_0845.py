# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150208_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebook',
            name='resource_link',
            field=models.CharField(help_text='Find a book or movie file available on the intranet and copy the link here, e.g. http://localserver/path/to/book.pdf', max_length=512, verbose_name='resource link'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='resource_link',
            field=models.CharField(help_text='Find a book or movie file available on the intranet and copy the link here, e.g. http://localserver/path/to/book.pdf', max_length=512, verbose_name='resource link'),
            preserve_default=True,
        ),
    ]
