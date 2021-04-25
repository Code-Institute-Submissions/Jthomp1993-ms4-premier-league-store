from django.shortcuts import render


def view_news(request):
    """ A view to render the news page """
    return render(request, 'news/news.html')
