from django.contrib import admin

from favorite.models import FavoriteProduct



@admin.register(FavoriteProduct)
class FavoriteProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product__name', 'user__username', 'added_at')
    list_display_links = ('product__name',)
    list_filter = ('added_at', )
    search_fields = ('product__name', 'user__username')