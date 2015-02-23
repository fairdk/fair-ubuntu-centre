from __future__ import unicode_literals
from __future__ import absolute_import

from django.contrib import admin

from . import models


class ComputerAdmin(admin.ModelAdmin):
    list_display = ("label", "last_installed", "created")


class ScreenAdmin(admin.ModelAdmin):
    list_display = ("label",)


class PrinterAdmin(admin.ModelAdmin):
    list_display = ("label",)


admin.site.register(models.Computer, ComputerAdmin)
admin.site.register(models.Screen, ScreenAdmin)
admin.site.register(models.Printer, PrinterAdmin)
