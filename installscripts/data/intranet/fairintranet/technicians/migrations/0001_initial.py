# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(help_text="Please input a label with type X1234567, i.e. 'C0012345'", max_length=64, verbose_name='label of computer', validators=[django.core.validators.RegexValidator(regex='[A-Z]', message="Please input a label with type X1234567, i.e. 'C0012345'")])),
                ('created', models.DateTimeField(null=True, verbose_name='last installed', blank=True)),
                ('modified', models.DateTimeField(null=True, verbose_name='last installed', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('inventory_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='technicians.Inventory')),
                ('last_installed', models.DateTimeField(null=True, verbose_name='last installed', blank=True)),
            ],
            options={
            },
            bases=('technicians.inventory',),
        ),
        migrations.CreateModel(
            name='LogMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(verbose_name='last installed')),
                ('technician', models.CharField(max_length=128, null=True, verbose_name='technician name', blank=True)),
                ('created', models.DateTimeField(null=True, verbose_name='last installed', blank=True)),
                ('modified', models.DateTimeField(null=True, verbose_name='last installed', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('inventory_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='technicians.Inventory')),
            ],
            options={
            },
            bases=('technicians.inventory',),
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('inventory_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='technicians.Inventory')),
            ],
            options={
            },
            bases=('technicians.inventory',),
        ),
        migrations.AddField(
            model_name='logmessage',
            name='inventory',
            field=models.ForeignKey(verbose_name='last installed', blank=True, to='technicians.Inventory', null=True),
            preserve_default=True,
        ),
    ]
