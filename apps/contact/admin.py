from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('name', )
    search_help_text = 'search here'


admin.site.register(Contact, ContactAdmin)
