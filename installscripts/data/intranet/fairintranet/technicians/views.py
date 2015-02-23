from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from . import models

def register_computer_installation(request, label=None):

    computer, created = models.Computer.objects.get_or_create(label=label)
    computer.last_installed = timezone.now()
    computer.save()

    return HttpResponse("OK")
