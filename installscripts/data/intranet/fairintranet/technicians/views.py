from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from . import models

def register_computer_installation(request, computer_label=None):

    computer, created = models.Computer.objects.get_or_create(label=computer_label)
    computer.installed = timezone.now()
    computer.save()

    return HttpResponse("OK")
