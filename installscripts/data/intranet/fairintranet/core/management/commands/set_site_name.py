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


from core import models


logger = logging.getLogger('fairintranet.core')


class Command(BaseCommand):
    help = (
        'Asks for institution name and sets it on the main page'
    )
    args = ''

    def handle(self, *args, **options):
        try:
            page = models.HomePage.get_root_nodes()[0].get_children()[0]
        except IndexError:
            logger.error("No root page")
            sys.exit(-1)
        
        school_name = raw_input("Enter the name of school/institution (Name Of School): ")
        school_name = school_name.strip()
        
        site_name = "Intranet of " + school_name
        page.title = site_name
        page.save()
        
        logger.info("New site name set: {:s}".format(site_name))
