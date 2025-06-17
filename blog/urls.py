from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('comment/delete/<int:comment_id>/', views.delete_post_comment, name='delete_post_comment'),
]