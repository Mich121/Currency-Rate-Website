from blog.views import AddPostView
from django.urls import path
from .views import AddCommentView, Articles, Article, UpdatePostView, DeletePostView, AddPostView, AddCommentView

urlpatterns = [
    path('articles/', Articles.as_view(), name='articles'),
    path('article/<int:pk>/', Article.as_view(), name='article'),
    path('article_update/<int:pk>/', UpdatePostView.as_view(), name='article_update'),
    path('article_delete/<int:pk>/', DeletePostView.as_view(), name='article_delete'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]