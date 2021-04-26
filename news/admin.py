from django.contrib import admin
from .models import News, Comments


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'heading',
        'description',
        'content',
        'image',
    )


admin.site.register(News, NewsAdmin,)
admin.site.register(Comments)

