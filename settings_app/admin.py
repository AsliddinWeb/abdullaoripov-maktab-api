from django.contrib import admin

from unfold.admin import ModelAdmin

from .models import (
    SeoSettings,
    HeaderSettings,
    FooterSettings,
    FooterLinkCategory,
    FooterLink,
    SocialSettings,
    MoreTitles,
    ErrorTexts
)

@admin.register(SeoSettings)
class SeoSettingsAdmin(ModelAdmin):
    list_display = ('title', 'author', 'site')
    search_fields = ('title', 'keywords', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'keywords', 'description', 'author', 'favicon', 'robots', 'site')
        }),
    )
    readonly_fields = ('favicon',)

@admin.register(HeaderSettings)
class HeaderSettingsAdmin(ModelAdmin):
    list_display = ('test_message', 'location', 'email')
    search_fields = ('test_message', 'location', 'email')
    fieldsets = (
        (None, {
            'fields': ('test_message', 'location_link', 'location', 'email_link', 'email', 'logo', 'logo_alt', 'search_placeholder')
        }),
    )
    readonly_fields = ('logo',)

@admin.register(FooterSettings)
class FooterSettingsAdmin(ModelAdmin):
    list_display = ('title', 'phone', 'footer_logo')
    search_fields = ('title', 'phone', 'body')
    fieldsets = (
        (None, {
            'fields': ('footer_logo', 'title', 'location', 'phone', 'body', 'copyright', 'note')
        }),
    )
    readonly_fields = ('footer_logo',)

@admin.register(FooterLinkCategory)
class FooterLinkCategoryAdmin(ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(FooterLink)
class FooterLinkAdmin(ModelAdmin):
    list_display = ('category', 'title', 'link')
    search_fields = ('title', 'link')
    list_filter = ('category',)
    autocomplete_fields = ('category',)

@admin.register(SocialSettings)
class SocialSettingsAdmin(ModelAdmin):
    list_display = ('title', 'i_class', 'link')
    search_fields = ('title', 'i_class', 'link')

@admin.register(MoreTitles)
class MoreTitlesAdmin(ModelAdmin):
    list_display = ('home', 'related_news', 'news_page')
    search_fields = ('home', 'related_news', 'news_page')

@admin.register(ErrorTexts)
class ErrorTextsAdmin(ModelAdmin):
    list_display = ('error_404_title', 'error_500_title')
    search_fields = ('error_404_title', 'error_404_body', 'error_500_title', 'error_500_body')
