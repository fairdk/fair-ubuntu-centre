from __future__ import unicode_literals
from __future__ import absolute_import
import os
import mimetypes
from datetime import datetime

from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.utils.http import http_date
from django.utils import dateformat

from . import models
from django.http.response import Http404


def send_file(request, filepath, last_modified=None, filename=None):
    fullpath = filepath
    # Respect the If-Modified-Since header.
    statobj = os.stat(fullpath)
    if filename:
        mimetype, encoding = mimetypes.guess_type(filename)
    else:
        mimetype, encoding = mimetypes.guess_type(fullpath)

    mimetype = mimetype or 'application/octet-stream'

    response = HttpResponse(open(fullpath, 'rb').read(), content_type=mimetype)

    if not last_modified:
        response["Last-Modified"] = http_date(statobj.st_mtime)
    else:
        if isinstance(last_modified, datetime):
            last_modified = float(dateformat.format(last_modified, 'U'))
        response["Last-Modified"] = http_date(epoch_seconds=last_modified)

    response["Content-Length"] = statobj.st_size

    if encoding:
        response["Content-Encoding"] = encoding

    if filename:
        response["Content-Disposition"] = "attachment; filename=%s" % filename
    
    return response


def download(request, resource_id):
    """Simple view for serving a file or redirect and conting stats"""
    resource = get_object_or_404(models.Resource, id=resource_id)
    models.ResourceUsage.count_click(resource)
    
    if resource.resource_link.startswith("http:"):
        return redirect(resource.resource_link)
    
    if not os.path.exists(resource.resource_link):
        raise Http404()
