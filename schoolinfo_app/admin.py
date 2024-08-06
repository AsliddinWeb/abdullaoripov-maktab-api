from django.contrib import admin

# Unfold admin
from unfold.admin import ModelAdmin, TabularInline

from .models import InfoImages, SchoolInfo, SchoolLeaders, Teachers, EducationSystem, Gallery, ApplyInfo

class SchoolInfoInline(TabularInline):
    model = SchoolInfo.images.through
    extra = 1

@admin.register(SchoolInfo)
class SchoolInfoAdmin(ModelAdmin):
    list_display = ('name', 'address', 'main_image')
    search_fields = ('name', 'address')
    filter_horizontal = ('images',)
    inlines = [SchoolInfoInline]

class EducationSystemInline(TabularInline):
    model = EducationSystem.images.through
    extra = 1

@admin.register(EducationSystem)
class EducationSystemAdmin(ModelAdmin):
    list_display = ('title', 'main_image')
    search_fields = ('title',)
    filter_horizontal = ('images',)
    inlines = [EducationSystemInline]

@admin.register(InfoImages)
class InfoImagesAdmin(ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)

@admin.register(SchoolLeaders)
class SchoolLeadersAdmin(ModelAdmin):
    list_display = ('name', 'position', 'phone', 'email')
    search_fields = ('name', 'position')

@admin.register(Teachers)
class TeachersAdmin(ModelAdmin):
    list_display = ('name', 'subject', 'phone', 'email')
    search_fields = ('name', 'subject')

@admin.register(Gallery)
class GalleryAdmin(ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)

@admin.register(ApplyInfo)
class ApplyInfoAdmin(ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)
