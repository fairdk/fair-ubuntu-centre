from __future__ import unicode_literals
from __future__ import absolute_import

from django import forms

from . import models


class LogMessageForm(forms.ModelForm):
    
    inventory = forms.ModelChoiceField(models.Inventory.objects.all(), widget=forms.HiddenInput())
    
    class Meta:
        model = models.LogMessage