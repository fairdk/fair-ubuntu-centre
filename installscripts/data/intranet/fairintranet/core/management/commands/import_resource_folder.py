from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import logging
import os
import sys

from django.core.management.base import BaseCommand

from optparse import make_option
from django.template.defaultfilters import slugify
from django.template.defaultfilters import striptags

from wagtailimages.models import Image

from core import models
from django.core.files.base import File


logger = logging.getLogger('fairintranet.core')


class Command(BaseCommand):
    help = (
        'Import a resource folder recursively. Adds all found and non-existing '
        'resources to a collection. For every filename.ext, you can place a '
        'special .filename.ext.description (text) and .filename.ext.image '
        'to import as description and thumbnail (JPEG format)'
    )
    args = '<folder_path> <collection_id>'

    option_list = BaseCommand.option_list + (
        make_option(
            '--replace_existing',
            action='store_true',
            dest='replace_existing',
            default=False,
            help='Replace existing resources'),
        make_option(
            '--delete_existing',
            action='store_true',
            dest='delete_existing',
            default=False,
            help='Delete non-existing existing resources'),
    )

    def handle(self, *args, **options):
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
        
        def add_to_collection(item):
            
            description_file = item + ".description"
            if os.path.isfile(description_file):
                description = open(description_file, 'r').read()
            else:
                description = ""
            
            title = os.path.basename(item)
            title = ".".join(".".split(title)[:-1])
            title = title.replace("_", " ")
            
            thumbnail_file = item + ".image"
            if os.path.isfile(description_file):
                thumbnail_path = open(thumbnail_file, 'r').read()
                f = open(thumbnail_path, 'r')
                image = Image()
                image.file.save(os.path.basename(item) + ".jpeg", File(f))
                image.title = "Thumbnail for " + title
                image.save()
            else:
                thumbnail = None
        
        def scan_folder(arg, dirname, names):
            for name in names:
                item = os.path.join(dirname, name)
                if os.path.isdir(item):
                    continue
                else:
                    add_to_collection(item)
        
        os.path.walk(args[0], scan_folder, None)
