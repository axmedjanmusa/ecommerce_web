from django.contrib import admin

from cart.models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    fields = ('product', 'quantity', 'get_item_cost')
    readonly_fields = ('get_item_cost',)
    extra = 3

    def get_item_cost(self, obj):
        return obj.get_cost()
    get_item_cost.short_description = 'Стоимость позиции'



@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'session_key', 'created_at', 'updated_at', 'get_total_cart_cost',
                    'get_total_cart_quantity')

    list_filter = ('created_at', 'updated_at', 'user')
    search_fields = ('user__username', 'session_key', 'id')
    readonly_fields = ('created_at', 'updated_at', 'get_total_cart_cost', 'get_total_cart_quantity')
    fields = ('user', 'session_key', 'created_at', 'updated_at', 'get_total_cart_cost', 'get_total_cart_quantity')
    inlines = [CartItemInline]



    def get_total_cart_cost(self, obj):
        return obj.get_total_cost()

    get_total_cart_cost.short_description = 'Общая цена'

    def get_total_cart_quantity(self, obj):
        return obj.get_total_quantity()

    get_total_cart_quantity.short_description = 'Всего товаров'