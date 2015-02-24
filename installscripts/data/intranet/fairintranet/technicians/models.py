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
        verbose_name=_("created"),
        blank=True,
        null=True,
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        verbose_name=_("modified"),
        blank=True,
        null=True,
        auto_now=True,
    )
    former_inventory = models.BooleanField(
        verbose_name=_("former inventory"),
        help_text=_("Means that the item is no longer at the facility"),
        default=False,
    )
    
    class Meta:
        ordering = ("label",)

    def __str__(self):
        return self.label.upper()


class Computer(Inventory):
    
    last_installed = models.DateTimeField(
        verbose_name=_("last installed"),
        blank=True,
        null=True,
    )

    def __str__(self):
        if not self.former_inventory:
            return "Computer {}".format(self.label.upper())
        return "Computer {} (removed)".format(self.label.upper())


class Screen(Inventory):
    
    def __str__(self):
        return "Screen {}".format(self.label.upper())


class Printer(Inventory):
    
    def __str__(self):
        return "Printer {}".format(self.label.upper())


class ComputerSession(models.Model):
    
    computer = models.ForeignKey('Computer')
    started = models.DateTimeField(auto_now_add=True)
    ended = models.DateTimeField(null=True, blank=True)
    username = models.CharField(blank=True, null=True, max_length=32)
    
    class Meta:
        verbose_name = _("Computer session")
        get_latest_by = "started"


class LogMessage(models.Model):
    
    inventory = models.ForeignKey(
        'Inventory',
        verbose_name=_("last installed"),
        blank=True,
        null=True,
    )
    message = models.TextField(
        verbose_name=_("message"),
    )
    technician = models.CharField(
        verbose_name=_("technician name"),
        blank=True,
        null=True,
        max_length=128,
    )
    created = models.DateTimeField(
        verbose_name=_("created"),
        blank=True,
        null=True,
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        verbose_name=_("modified"),
        blank=True,
        null=True,
        auto_now=True,
    )
    resolved = models.BooleanField(
        verbose_name=_("has been resolved"),
        default=False,
    )
    removed = models.BooleanField(
        verbose_name=_("removed this inventory"),
        default=False,
    )
    
    class Meta:
        verbose_name = _("Log message")
        get_latest_by = "created"
    
    def save(self, force_insert=False, force_update=False, using=None, 
        update_fields=None):
        if self.removed:
            self.inventory.former_inventory = True
            self.inventory.save()
        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
    
