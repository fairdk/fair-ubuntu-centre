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
        'Creates thumbnails recursively in <target dir>'
    )
    args = '<target dir>'

    def handle(self, *args, **options):
        
        if not len(args) == 1:
            logger.error("Only takes 1 argument")
            sys.exit(-1)
        if not os.path.isdir(args[0]):
            logger.error("Target not found: {:s}".format(args[0]))
            sys.exit(-1)
        
        try:
            from anythumbnailer.thumbnail_ import create_thumbnail
        except ImportError:
            logger.error("You need anythumbnailer. Install with:")
            logger.error("  sudo pip install -e git+git://github.com/FelixSchwarz/anythumbnailer.git#egg=anythumbnailer")
            sys.exit(-1)
        
        def scan_folder(arg, dirname, names):
            for name in names:
                item = os.path.join(dirname, name)
                if os.path.isdir(item):
                    continue
                if item.endswith(".thumbnail"):
                    continue
                fp = create_thumbnail(item, output_format='jpg')
                file(item + ".thumbnail", 'wb').write(thumbnail_fp.read())
        
        os.path.walk(args[0], scan_folder, None)
        
        logger.info("Moved all resources point at {:s} to {:s}".format(old_location, new_location))