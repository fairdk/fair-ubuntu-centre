from __future__ import unicode_literals
from __future__ import absolute_import

from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import settings


class Inventory(models.Model):
    
    label = models.CharField(
        max_length=64,
        verbose_name=_("label of computer"),
        help_text=settings.LABEL_VALIDATION_HELP,
        validators=[RegexValidator(
            regex=settings.LABEL_VALIDATION,
            message=settings.LABEL_VALIDATION_HELP,
        )]
    )
    created = models.DateTimeField(
        verbose_name=_("last installed"),
        blank=True,
        null=True,
    )
    modified = models.DateTimeField(
        verbose_name=_("last installed"),
        blank=True,
        null=True,
    )


class Computer(Inventory):
    
    last_installed = models.DateTimeField(
        verbose_name=_("last installed"),
        blank=True,
        null=True,
    )


class Screen(Inventory):
    
    pass


class Printer(Inventory):
    
    pass


class LogMessage(models.Model):
    
    inventory = models.ForeignKey(
        'Inventory',
        verbose_name=_("last installed"),
        blank=True,
        null=True,
    )
    message = models.TextField(
        verbose_name=_("last installed"),
    )
    technician = models.CharField(
        verbose_name=_("technician name"),
        blank=True,
        null=True,
        max_length=128,
    )
    created = models.DateTimeField(
        verbose_name=_("last installed"),
        blank=True,
        null=True,
    )
    modified = models.DateTimeField(
        verbose_name=_("last installed"),
        blank=True,
        null=True,
    )
