# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150209_0845'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceUsage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clicks', models.PositiveIntegerField(default=0)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('ebook', models.ForeignKey(blank=True, to='core.EBook', null=True)),
                ('movie', models.ForeignKey(blank=True, to='core.Movie', null=True)),
            ],
            options={
                'ordering': ('from_date', 'to_date'),
                'verbose_name': 'resource usage',
                'verbose_name_plural': 'resource usages',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Standard articles'},
        ),
    ]
