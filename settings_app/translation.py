from modeltranslation.translator import register, TranslationOptions

from .models import (
    SeoSettings,
    HeaderSettings,
    FooterSettings,
    FooterLinkCategory,
    FooterLink,
    MoreTitles,
    ErrorTexts,
)

@register(SeoSettings)
class SeoSettingsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(HeaderSettings)
class HeaderSettingsTranslationOptions(TranslationOptions):
    fields = ('test_message', 'location', 'logo_alt', 'search_placeholder')

@register(FooterSettings)
class FooterSettingsTranslationOptions(TranslationOptions):
    fields = ('title', 'location', 'body', 'copyright', 'note')

@register(FooterLinkCategory)
class FooterLinkCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(FooterLink)
class FooterLinkTranslationOptions(TranslationOptions):
    fields = ('title', )

@register(MoreTitles)
class MoreTitlesTranslationOptions(TranslationOptions):
    fields = ('home', 'related_news', 'news_page', 'search_title', 'news_category_title', 'share', 'empty_news')

@register(ErrorTexts)
class ErrorTextsTranslationOptions(TranslationOptions):
    fields = ('error_404_title', 'error_404_body', 'error_500_title', 'error_500_body')
