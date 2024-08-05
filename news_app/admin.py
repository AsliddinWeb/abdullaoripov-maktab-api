from django.contrib import admin

# Unfold admin
from unfold.admin import ModelAdmin

from .models import Category, News, NewsImage, NewsDetailText

class CategoryAdmin(ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

class NewsImageInline(admin.TabularInline):
    model = News.images.through
    extra = 1

class NewsAdmin(ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'body')
    list_filter = ('category', 'created_at')
    filter_horizontal = ('images',)
    inlines = [NewsImageInline]

class NewsImageAdmin(ModelAdmin):
    list_display = ('id', 'image', 'created_at')

admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(NewsImage, NewsImageAdmin)

class NewsDetailTextAdmin(ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
admin.site.register(NewsDetailText, NewsDetailTextAdmin)