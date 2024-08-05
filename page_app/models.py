from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Sarlavha"))
    slug = models.SlugField(max_length=200, unique=True, verbose_name=_("Slug"))
    content = RichTextField(verbose_name=_("Kontent"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan sana"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan sana"))

    class Meta:
        verbose_name = _("Sahifa")
        verbose_name_plural = _("Sahifalar")

    def __str__(self):
        return self.title


class File(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Fayl nomi"))
    file = models.FileField(upload_to='pages/files/', verbose_name=_("Faylni yuklang"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Fayllar"
        verbose_name_plural = "Fayllar"
