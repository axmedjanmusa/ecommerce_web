# favorite/urls.py
from django.urls import path
from . import views

app_name = 'favorite'

urlpatterns = [
    path('', views.favorite_list, name='favorite_list'),
    path('add/<int:product_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove/<int:product_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('toggle/<int:product_id>/', views.toggle_favorite, name='toggle_favorite'),  # Add this pattern
]