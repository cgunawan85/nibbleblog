from django.contrib import admin

from .models import Article, Entry


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', ]
    list_filter = ['created_at', ]
    list_display = ['title', 'user', 'created_at', ]


class EntryAdmin(admin.ModelAdmin):
    search_fields = ['restaurant_name', ]
    list_filter = ['created_at', ]
    list_display = ['restaurant_name', 'article', ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Entry, EntryAdmin)
