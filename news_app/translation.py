from modeltranslation.translator import register, TranslationOptions

from .models import Category, News, NewsDetailText

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

@register(NewsDetailText)
class NewsDetailTextTranslationOptions(TranslationOptions):
    fields = ('title',)
