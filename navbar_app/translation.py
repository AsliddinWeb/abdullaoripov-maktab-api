from modeltranslation.translator import register, TranslationOptions
from .models import OneNavbar, TwoNavbar, ThreeNavbar

@register(OneNavbar)
class OneNavbarTranslationOptions(TranslationOptions):
    fields = ('title', )

@register(TwoNavbar)
class TwoNavbarTranslationOptions(TranslationOptions):
    fields = ('title', )

@register(ThreeNavbar)
class ThreeNavbarTranslationOptions(TranslationOptions):
    fields = ('title', )
