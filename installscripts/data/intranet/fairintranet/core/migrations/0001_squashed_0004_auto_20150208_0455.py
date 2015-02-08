# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailcore.fields


def create_homepage(apps, schema_editor):
    # Get models
    ContentType = apps.get_model('contenttypes.ContentType')
    Page = apps.get_model('wagtailcore.Page')
    Site = apps.get_model('wagtailcore.Site')
    HomePage = apps.get_model('core.HomePage')

    # Delete the default homepage
    Page.objects.get(id=2).delete()

    # Create content type for homepage model
    homepage_content_type, created = ContentType.objects.get_or_create(
        model='homepage', app_label='core', defaults={'name': 'Homepage'})

    # Create a new homepage
    homepage = HomePage.objects.create(
        title="Homepage",
        slug='home',
        content_type=homepage_content_type,
        path='00010001',
        depth=2,
        numchild=0,
        url_path='/home/',
    )

    # Create a site with the new homepage set as the root
    Site.objects.create(
        hostname='localhost', root_page=homepage, is_default_site=True)


# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# core.migrations.0001_squashed_0005_auto_20150207_2353


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtailcore', '__latest__'),
        ('wagtailforms', '0001_initial'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('wagtailredirects', '0001_initial'),
        ('wagtailsearch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RunPython(
            code=create_homepage,
            reverse_code=None,
            atomic=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='cover_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='EBook',
            fields=[
                ('homepage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.HomePage')),
                ('author', models.CharField(max_length=64, null=True, verbose_name='author / director', blank=True)),
                ('country', models.CharField(max_length=64, null=True, verbose_name='country of origin', blank=True)),
                ('resource_link', models.URLField(default='', help_text='Find a book or movie file available on the intranet and copy the link here, e.g. http://localserver/path/to/book.pdf', verbose_name='resource link')),
                ('thumbnail', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
                ('year', models.PositiveSmallIntegerField(null=True, verbose_name='year of publication', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.homepage',),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('homepage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.HomePage')),
                ('year', models.PositiveSmallIntegerField(null=True, verbose_name='year of publication', blank=True)),
                ('country', models.CharField(max_length=64, null=True, verbose_name='country of origin', blank=True)),
                ('author', models.CharField(max_length=64, null=True, verbose_name='author / director', blank=True)),
                ('resource_link', models.URLField(default='http://dr.dk', help_text='Find a book or movie file available on the intranet and copy the link here, e.g. http://localserver/path/to/book.pdf', verbose_name='resource link')),
                ('thumbnail', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.homepage',),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name='Body / main text on page', blank=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('homepage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.HomePage')),
                ('icon', models.ImageField(help_text='Cheerful icon to display on buttons next to the title', upload_to=b'', null=True, verbose_name='icon', blank=True)),
                ('license', models.CharField(max_length=64, null=True, verbose_name='license', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.homepage',),
        ),
        migrations.CreateModel(
            name='ExternalCollection',
            fields=[
                ('collection_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.Collection')),
                ('retrieved', models.DateField(help_text='When this collection was copied from the internet', null=True, verbose_name='Retrieval date', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.collection',),
        ),
        migrations.AddField(
            model_name='collection',
            name='button_caption',
            field=models.CharField(max_length=64, null=True, verbose_name='button caption', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='collection',
            name='icon',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', help_text='Cheerful icon to display on buttons next to the title', null=True, verbose_name='icon'),
            preserve_default=True,
        ),
    ]
