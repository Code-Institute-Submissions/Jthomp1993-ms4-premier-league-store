from django.shortcuts import render
from .models import News


def view_news(request):
    """ A view to render the news page """
    news = News.objects.all()

    context = {
        'news': news,
    }

    return render(request, 'news/news.html', context)
