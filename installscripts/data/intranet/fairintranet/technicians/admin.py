from __future__ import unicode_literals
from __future__ import absolute_import

from django.contrib import admin

from . import models


class ComputerAdmin(admin.ModelAdmin):
    pass


class ScreenAdmin(admin.ModelAdmin):
    pass


class PrinterAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Computer, ComputerAdmin)
admin.site.register(models.Screen, ScreenAdmin)
admin.site.register(models.Printer, PrinterAdmin)