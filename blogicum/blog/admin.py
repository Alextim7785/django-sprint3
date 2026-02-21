from django.contrib import admin

from .models import Category, Location, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'slug',
        'is_published',
        'created_at'
    )
    list_editable = (
        'is_published',
        'created_at'
    )
    search_fields = ('title',)
    list_filter = ('created_at',)
    list_display_links = ('title',)


admin.site.register(Category, CategoryAdmin)


class LocatoinAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_filter = ('created_at',)


admin.site.register(Location, LocatoinAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'category',
        'is_published',
        'created_at'
    )
    list_editable = (
        'is_published',
        'author',
        'location',
        'category',
        'is_published'
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)


admin.site.register(Post, PostAdmin)
