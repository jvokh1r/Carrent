from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    search_fields = ('author', 'created_at', 'post')
    search_help_text = 'search here'


admin.site.register(Comment, CommentAdmin)

