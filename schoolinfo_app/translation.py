from modeltranslation.translator import register, TranslationOptions

from .models import InfoImages, SchoolInfo, SchoolLeaders, Teachers, EducationSystem, Gallery, ApplyInfo

@register(InfoImages)
class InfoImagesTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(SchoolInfo)
class SchoolInfoTranslationOptions(TranslationOptions):
    fields = ('name', 'address', 'content')

@register(SchoolLeaders)
class SchoolLeadersTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'education')

@register(Teachers)
class TeachersTranslationOptions(TranslationOptions):
    fields = ('name', 'subject', 'education')

@register(EducationSystem)
class EducationSystemTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(ApplyInfo)
class ApplyInfoTranslationOptions(TranslationOptions):
    fields = ('title',)
