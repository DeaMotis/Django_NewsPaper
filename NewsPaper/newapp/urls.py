from django.urls import path

from .views import PostCreate, PostEdit, PostDelete, ArticleCreate, ArticleEdit, ArticleDelete, PostList, PostDetail, PostSearch



urlpatterns = [

    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('search', PostSearch.as_view(), name='post_list'),

    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', ArticleEdit.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
]