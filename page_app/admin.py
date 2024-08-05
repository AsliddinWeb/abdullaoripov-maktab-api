from django.contrib import admin

# Unfold admin
from unfold.admin import ModelAdmin

from .forms import PageAdminForm
from .models import Page, File

@admin.register(Page)
class PageAdmin(ModelAdmin):
    form = PageAdminForm
    list_display = ('title', 'slug', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(File)
class FileAdmin(ModelAdmin):
    list_display = ('title', 'file')
