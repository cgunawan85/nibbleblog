from django.contrib import admin

from .models import Article, Entry


class EntryInline(admin.StackedInline):
    model = Entry
    search_fields = ['restaurant_name', ]
    list_filter = ['created_at', ]
    list_display = ['restaurant_name', 'article', ]

    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 12
        return max_num


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', ]
    list_filter = ['created_at', ]
    list_display = ['title', 'user', 'created_at', ]
    inlines = [
        EntryInline,
    ]


admin.site.register(Article, ArticleAdmin)
