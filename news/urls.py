from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_news, name='news'),
    path('<int:news_id>', views.news_detail, name='news_detail'),
    path('addcomment/<int:news_id>/', views.add_comment, name='add_comment'),
    path('deletecomment/<int:news_id>/<int:comment_id>/',
         views.delete_comment, name='delete_comment'),
    path('editcomment/<int:news_id>/<int:comment_id>/',
         views.edit_comment, name='edit_comment'),
    path('addnews/', views.add_news, name='add_news'),
    path('edit_news/<int:news_id>/',
         views.edit_news, name='edit_news'),
    path('deletenews/<int:news_id>/',
         views.delete_news, name='delete_news'),
]