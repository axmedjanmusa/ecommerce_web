from django.urls import path
from . import views
from .views import cart_detail

app_name = 'cart'
urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('remove/<int:item_id>/', views.remove_cart_item, name='remove_cart_item'),

]
