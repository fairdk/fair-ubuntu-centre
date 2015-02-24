# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technicians', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('started', models.DateTimeField(auto_now_add=True)),
                ('ended', models.DateTimeField(null=True, blank=True)),
                ('username', models.CharField(max_length=32, null=True, blank=True)),
                ('computer', models.ForeignKey(to='technicians.Computer')),
            ],
            options={
                'get_latest_by': 'started',
                'verbose_name': 'Computer session',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='logmessage',
            options={'get_latest_by': 'created', 'verbose_name': 'Log message'},
        ),
        migrations.AddField(
            model_name='inventory',
            name='former_inventory',
            field=models.BooleanField(default=False, help_text='Means that the item is no longer at the facility', verbose_name='former inventory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='logmessage',
            name='removed',
            field=models.BooleanField(default=False, verbose_name='has been resolved'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='logmessage',
            name='resolved',
            field=models.BooleanField(default=False, verbose_name='has been resolved'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inventory',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inventory',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified', null=True),
            preserve_default=True,
        ),
    ]
