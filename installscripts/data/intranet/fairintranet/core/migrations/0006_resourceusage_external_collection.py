# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150222_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourceusage',
            name='external_collection',
            field=models.ForeignKey(blank=True, to='core.ExternalCollection', null=True),
            preserve_default=True,
        ),
    ]
