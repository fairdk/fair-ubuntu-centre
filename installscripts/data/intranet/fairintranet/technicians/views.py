from __future__ import unicode_literals
from __future__ import absolute_import

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone

from . import forms
from . import models
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


class ComputerList(ListView):
    
    template_name = "technicians/computer_list.html"
    model = models.Computer
    context_object_name = "computers"


class ComputerLog(DetailView):
    
    template_name = "technicians/computer_log.html"
    model = models.Computer
    context_object_name = "computer"
    
    def get_context_data(self, **kwargs):
        c = DetailView.get_context_data(self, **kwargs)
        c['log_messages'] = models.LogMessage.objects.filter(inventory=c['computer'])
        c['log_form'] = forms.LogMessageForm(initial={'inventory': c['computer']})
        return c


class ComputerLogAdd(CreateView):
    
    model = models.LogMessage
    form_class = forms.LogMessageForm
    template_name = "technicians/log_message_add.html"
    
    def dispatch(self, request, *args, **kwargs):
        self.computer = get_object_or_404(models.Computer, pk=kwargs.pop('pk'))
        return CreateView.dispatch(self, request, *args, **kwargs)
    
    def form_valid(self, form):
        log = form.save()
        return redirect("technicians:computer_log", pk=log.inventory.pk)
    
    def get_context_data(self, **kwargs):
        c = CreateView.get_context_data(self, **kwargs)
        c['computer'] = self.computer
        return c
    
    def get_initial(self):
        return {'inventory': self.computer}


def register_computer_installation(request, label=None):

    computer, __ = models.Computer.objects.get_or_create(label=label)
    computer.last_installed = timezone.now()
    computer.save()

    return HttpResponse("OK")


def computer_login(request, label="", user=""):
    
    computer = get_object_or_404(models.Computer, label__iexact=label)
    
    models.ComputerSession.objects.create(
        computer=computer,
        username=user
    )

    return HttpResponse("OK")


def computer_logout(request, label="", user=""):
    
    computer = get_object_or_404(models.Computer, label__iexact=label)
    
    models.ComputerSession.objects.filter(
        computer=computer,
        username=user,
        ended=None,
    ).update(ended=timezone.now())

    return HttpResponse("OK")
