from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import logging
import os
import sys

from django.core.management.base import BaseCommand

from core import models


logger = logging.getLogger('fairintranet.core')


class Command(BaseCommand):
    help = (
        'If media is changed, this command will change all resource links '
        'pointing at /old/destination to /new/destination'
    )
    args = '<old root dir> <new root dir>'

    def handle(self, *args, **options):
        
        if not len(args) == 2:
            logger.error("Only takes 2 arguments")
            sys.exit(-1)
        if not os.path.isdir(args[1]):
            logger.error("Destination not found: {:s}".format(args[1]))
            sys.exit(-1)
        
        if not args[0].startswith("/") or not args[1].startswith("/"):
            logger.error("Source and target must be absolute, i.e. start with /")
            sys.exit(-1)
        
        old_location = args[0]
        new_location = args[1]
        
        if not old_location.endswith("/"):
            old_location += "/"
        
        if not new_location.endswith("/"):
            new_location += "/"
            
        movies = list(models.Movie.objects.filter(resource_link__istartswith=args[0]))
        ebooks = list(models.EBook.objects.filter(resource_link__istartswith=args[0]))
        
        for item in movies + ebooks:
            item.resource_link = item.resource_link[len(old_location):]
            item.resource_link = new_location + item.resource_link
            item.save()
        
        logger.info("Moved all resources point at {:s} to {:s}".format(old_location, new_location))