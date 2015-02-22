from django.contrib import admin

from . import models


class ResourceUsageAdmin(admin.ModelAdmin):
    list_display = ('resource_name', 'clicks', 'from_date', 'to_date')
    
    def resource_name(self, instance):
        if instance.ebook:
            return "Ebook: {}".format(instance.ebook.title)
        if instance.movie:
            return "Movie: {}".format(instance.movie.title)
    

admin.site.register(models.ResourceUsage, ResourceUsageAdmin)