from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_news, name='news'),
    path('<news_id>', views.news_detail, name='news_detail'),
]