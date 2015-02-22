from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import logging
import os
import sys

from django.core.management.base import BaseCommand

from optparse import make_option


logger = logging.getLogger('fairintranet.core')


class Command(BaseCommand):
    help = (
        'Creates thumbnails recursively in <target dir>'
    )
    args = '<target dir>'

    option_list = BaseCommand.option_list + (
        make_option(
            '--overwrite-existing',
            action='store_true',
            dest='overwrite_existing',
            default=False,
            help='Recreates thumbnails even if they already exist'),
    )

    def handle(self, *args, **options):
        
        if not len(args) == 1:
            logger.error("Only takes 1 argument")
            sys.exit(-1)
        if not os.path.isdir(args[0]):
            logger.error("Target not found: {:s}".format(args[0]))
            sys.exit(-1)
        
        from .anythumbnailer.thumbnail_ import create_thumbnail
        
        thumbnails_created = []
        
        def scan_folder(thumbnails_created, dirname, names, ):
            for name in names:
                item = os.path.join(dirname, name)
                if os.path.isdir(item):
                    continue
                if item.endswith(".thumbnail"):
                    continue
                thumb_path = item + '.thumbnail'
                if not options['overwrite_existing'] and os.path.isfile(thumb_path):
                    continue
                fp = create_thumbnail(item, output_format='jpg')
                if fp:
                    contents = fp.read()
                    if contents:
                        file(thumb_path, 'wb').write(contents)
                        thumbnails_created.append(thumb_path)
                    else:
                        logger.info("Skipping {:s}, cannot read".format(os.path.basename(item)))
        
        os.path.walk(args[0], scan_folder, thumbnails_created)
        
        logger.info("Created thumbnails for {:d} files".format(len(thumbnails_created)))
