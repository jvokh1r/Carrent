from django.contrib import admin
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )
    search_help_text = 'search here'


admin.site.register(Service, ServiceAdmin)