from modeltranslation.translator import register, TranslationOptions

from .models import HomeWelcome, HomeAbout, Counter, HomeLeaders

@register(HomeWelcome)
class HomeWelcomeTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'button_text')

@register(HomeAbout)
class HomeAboutTranslationOptions(TranslationOptions):
    fields = ('cap_title', 'title', 'content',
              'cap_title_1', 'title_1',
              'cap_title_2', 'title_2',
              'button_text')

@register(Counter)
class CounterTranslationOptions(TranslationOptions):
    fields = ('title', 'value')

@register(HomeLeaders)
class HomeLeadersTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'content')

