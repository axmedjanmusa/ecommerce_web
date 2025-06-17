from django.contrib import admin

from blog.models import *


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'slug')
    prepopulated_fields = {'slug': ('title', )}
    list_display_links = ('title',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'category')


@admin.register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
