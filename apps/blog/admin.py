from django.contrib import admin
from .models import Article, About, Team, History, HowItWorks, Category, Tag


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )
    search_help_text = 'search here'


class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )
    search_help_text = 'search here'


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'role')
    search_help_text = 'search here'


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )
    search_help_text = 'search here'


class HowItWorksAdmin(admin.ModelAdmin):
    list_display = ('hiw_title', )
    search_fields = ('hiw_title', )
    search_help_text = 'search here'


admin.site.register(Article, ArticleAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(HowItWorks, HowItWorksAdmin)

admin.site.register(Category)
admin.site.register(Tag)