from django.urls import path

from shop.views import *
from . import views
app_name = 'shop'


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]