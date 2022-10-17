from django.contrib import admin
from .models import Cars, Book


class CarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'trans')
    search_help_text = 'search here'


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'where_from', 'where_to')
    search_fields = ('car', 'where_from', 'where_to')
    search_help_text = 'search here'


admin.site.register(Cars, CarsAdmin)
admin.site.register(Book, BookAdmin)

