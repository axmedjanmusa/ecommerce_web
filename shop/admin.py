from django.contrib import admin

from shop.models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 5
    fk_name = 'product'

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" style="object-fit:contain;" />'
        return "-"

    image_preview.short_description = 'Миниатюра'
    image_preview.allow_tags = True


class ProductCharacteristicsInline(admin.TabularInline):
    model = ProductCharacteristics
    extra = 5
    fk_name = 'product'



@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_at', 'parent')
    prepopulated_fields = {'slug': ('name', )}
    list_display_links = ('name',)
    search_fields = ('name', 'slug')
    list_filter = ('parent', 'created_at')
    ordering = ('-created_at',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'stock', 'available', 'created_at', 'updated_at',)
    list_filter = ('category', 'available', 'created_at',)
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', )}
    list_editable = ('available',)
    ordering = ('-created_at',)
    list_display_links = ('name',)
    inlines = [ProductImageInline, ProductCharacteristicsInline]

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image')

@admin.register(ProductCharacteristics)
class ProductCharacteristicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'title', 'value')
    search_fields = ('title', 'value')
