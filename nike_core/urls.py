from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from blog.views import *



urlpatterns = [
    path('admin/', admin.site.urls),

    # redirect
    path('', lambda request: redirect('admin/', permanent=True)),

    # apps apis
    path('blog/', include('blog.urls')),
    path('shop/', include('shop.urls')),
    path('cart/', include('cart.urls')),
    path('user/', include('user.urls')),
    path('favorite/', include('favorite.urls')),
    path('test-404/', custom_404_view, name='test_404_page'),


    # urls для страниц
    path('home/', home_view, name='home'),

    # ckeditor
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
