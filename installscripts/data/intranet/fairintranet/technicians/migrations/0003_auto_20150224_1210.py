# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technicians', '0002_auto_20150224_1042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'ordering': ('label',)},
        ),
        migrations.AlterField(
            model_name='logmessage',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='logmessage',
            name='message',
            field=models.TextField(verbose_name='message'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='logmessage',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='logmessage',
            name='removed',
            field=models.BooleanField(default=False, verbose_name='removed this inventory'),
            preserve_default=True,
        ),
    ]
