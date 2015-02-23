from __future__ import print_function
from __future__ import unicode_literals

import logging
import os
import sys

from django.core.management.base import BaseCommand

from optparse import make_option
from django.template.defaultfilters import slugify
from django.template.defaultfilters import striptags

from django.core.files.base import File


logger = logging.getLogger('fairintranet.core')


# These extensions will create a Movie object instead of the
# default EBook
MOVIE_EXTENSIONS = ('avi', 'mp4', 'iso', 'xvid', 'mkv', 'pls', 'm3u', 'ogv')

EBOOK_EXTENSIONS = (
    'pdf', 'odt', 'doc', 'docx', 'ods', 'xls', 'xslx',
    'ps', 'odp', 'ppt', 'pptx', 'epub', 'txt'
)


class Command(BaseCommand):
    help = (
        'Import a resource folder recursively. Adds all found and non-existing '
        'resources to a collection. For every filename.ext, you can place a '
        'special .filename.ext.description.txt (text) and .filename.ext.thumbnail.jpeg '
        'to import as description and thumbnail (JPEG format). You can '
        'use the create_thumbnails management command to automatically create '
        'thumbnails.'
    )
    args = '<folder_path> <collection_id>'

    option_list = BaseCommand.option_list + (
        make_option(
            '--author',
            action='store',
            dest='author',
            default="",
            help='Sets the author fixed on everything imported'),
    )

    def handle(self, *args, **options):

        from wagtail.wagtailimages.models import Image
        from core import models

        try:
            collection = models.Collection.objects.get(id=args[1])
        except models.Collection.DoesNotExist:
            logger.error('Collection not found: {:s}'.format(args[1]))
            sys.exit(-1)
        except IndexError:
            logger.error('You need to supply two arguments: folder_path collection_id')
            sys.exit(-1)
        
        if not os.path.exists(args[0]):
            logger.error('Path not found: {:s}'.format(args[0]))
            sys.exit(-1)
        
        def add_to_collection(item, collection):
            
            description_file = item + ".description.txt"
            if os.path.isfile(description_file):
                description = open(description_file, 'r').read()
            else:
                description = ""
            
            file_name = os.path.basename(item)
            title = ".".join(file_name.split(".")[:-1])
            title = title.replace("_", " ")
            
            thumbnail_file = item + ".thumbnail.jpeg"
            if os.path.isfile(thumbnail_file):
                f = open(thumbnail_file, 'r')
                thumbnail = Image()
                thumbnail.file.save(os.path.basename(item) + ".jpeg", File(f))
                thumbnail.title = "Thumbnail for " + title
                thumbnail.save()
            else:
                thumbnail = None
            
            extension = file_name.split(".")[-1]
            if extension in MOVIE_EXTENSIONS:
                cls = models.Movie
            elif extension in EBOOK_EXTENSIONS:
                cls = models.EBook
            else:
                return
            
            slug = slugify(title)
            path = collection.path + "{pos:s}".format(pos=str(collection.numchild + 1).zfill(4))
            try:
                 obj = collection.get_children().filter(slug=slug)[0]
                 # Ensure that other objects with same slug and path are deleted
                 others = collection.get_children().filter(slug=slug).exclude(id=obj.id)
                 if others.exists():
                     logger.warn("Other objects with same path existed and were deleted. File: " + item)
                     others.delete()
            except IndexError:
                 obj = cls(path=path)
            obj.numchild=0
            obj.depth=collection.depth + 1
            obj.show_in_menus=False
            obj.resource_link=item
            obj.url_path=os.path.join(collection.url_path, slug) + "/"
            obj.slug=slug
            obj.title=title
            obj.live=True
            obj.short_description=description
            obj.author=options["author"]
            obj.duration=""
            obj.thumbnail=thumbnail 
            obj.save()
    
            collection.numchild += 1
            collection.save()
                    
        def scan_folder(collection, dirname):
            for name in os.listdir(dirname):
                if name.endswith(".thumbnail.jpeg") or name.endswith(".description.txt"):
                    continue
                item = os.path.join(dirname, name)
                if os.path.isdir(item):
                    title = name
                    slug = slugify(title)
                    path = collection.path + "{pos:s}".format(pos=str(collection.numchild + 1).zfill(4))
                    try:
                         obj = models.Collection.objects.get(path=path)
                    except models.Collection.DoesNotExist:
                         obj = models.Collection(path=path)
                    obj.numchild=0 
                    obj.depth=collection.depth + 1 
                    obj.show_in_menus=False 
                    obj.url_path=os.path.join(collection.url_path, slug) + "/" 
                    obj.slug=slug 
                    obj.title=title 
                    obj.live=True 
                    obj.short_description=""
                    obj.duration="" 
                    obj.save()

                    collection.numchild += 1
                    collection.save()
                    scan_folder(obj, item)
                else:
                    add_to_collection(item, collection)

        scan_folder(collection, args[0])
