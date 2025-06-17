from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('register/', views.registration_view, name='registration_url'),
    path('login/', views.login_view, name='login_url'),
    path('logout/', views.logout_view, name='logout_view'),
    path('profile/<int:user_id>/', views.profile_view, name='profile_view'),
    path('update_profile/', views.update_profile, name='update_profile'),
]