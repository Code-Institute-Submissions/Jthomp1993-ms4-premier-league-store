from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'heading',
        'description',
        'content',
        'image',
    )


admin.site.register(News, NewsAdmin)

