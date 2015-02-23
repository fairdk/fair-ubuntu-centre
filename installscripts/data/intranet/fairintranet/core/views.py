from __future__ import unicode_literals
from __future__ import absolute_import
import os
import mimetypes
from datetime import datetime

from django.shortcuts import redirect, get_object_or_404
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


def download_movie(request, movie_id, cls=models.Movie):
    """Simple view for serving a file or redirect and conting stats"""
    movie = get_object_or_404(models.Movie, id=movie_id)
    models.ResourceUsage.count_click(movie=movie)
    return download(movie)


def download_ebook(request, ebook_id, cls=models.Movie):
    """Simple view for serving a file or redirect and conting stats"""
    ebook = get_object_or_404(models.Movie, id=ebook_id)
    models.ResourceUsage.count_click(ebook=ebook)
    return download(ebook)


def download_external_collection(request, external_collection_id, cls=models.Movie):
    """Simple view for serving a file or redirect and conting stats"""
    external_collection = get_object_or_404(models.ExternalCollection, id=external_collection_id)
    models.ResourceUsage.count_click(external_collection=external_collection)
    return download(external_collection)


def download(resource):
    if resource.resource_link.startswith("http:"):
        return redirect(resource.resource_link)
    
    if not os.path.exists(resource.resource_link):
        raise Http404()
