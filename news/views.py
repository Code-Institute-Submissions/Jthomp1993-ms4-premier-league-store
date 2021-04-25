from django.shortcuts import render, get_object_or_404
from .models import News


def view_news(request):
    """ A view to render the news page """
    news = News.objects.all()

    context = {
        'news': news,
    }

    return render(request, 'news/news.html', context)


def news_detail(request, news_id):
    """ A view to render the news detail page """
    news = get_object_or_404(News, pk=news_id)

    context = {
        'news': news,
    }

    return render(request, 'news/news_detail.html', context)
