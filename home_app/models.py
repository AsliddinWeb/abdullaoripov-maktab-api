from django.db import models
from django.utils.translation import gettext_lazy as _

class HomeWelcome(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Sarlavha"))
    content = models.TextField(verbose_name=_("Matn"))

    button_text = models.TextField(verbose_name=_("Tugmacha matni"))
    button_link = models.CharField(max_length=255, verbose_name=_("Tugmacha manzili"))

    image = models.ImageField(upload_to='home/', verbose_name=_("Bosh sahifa rasmi"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "1. Bosh sahifa kirish qismi"
        verbose_name_plural = "1. Bosh sahifa kirish qismi"

class HomeAbout(models.Model):
    image = models.ImageField(upload_to='home/about/', verbose_name=_("Rasm"))
    cap_title = models.CharField(max_length=255, verbose_name=_("Kichik sarlavha"))
    title = models.CharField(max_length=255, verbose_name=_("Sarlavha"))
    content = models.TextField(verbose_name=_("Asosiy matn"))

    icon_1 = models.ImageField(upload_to='home/icons/', verbose_name=_("1-ikonka"))
    cap_title_1 = models.CharField(max_length=255, verbose_name=_("1-Kichik sarlavha"))
    title_1 = models.CharField(max_length=255, verbose_name=_("1-Sarlavha"))

    icon_2 = models.ImageField(upload_to='home/icons/', verbose_name=_("2-ikonka"))
    cap_title_2 = models.CharField(max_length=255, verbose_name=_("2-Kichik sarlavha"))
    title_2 = models.CharField(max_length=255, verbose_name=_("2-Sarlavha"))

    button_text = models.CharField(max_length=255, verbose_name=_("Tugmacha matni"))
    button_link = models.CharField(max_length=255, verbose_name=_("Tugmacha manzili"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "2. Biz haqimizda"
        verbose_name_plural = "2. Biz haqimizda"

class Counter(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Nomi"))
    value = models.CharField(max_length=255, verbose_name=_("Soni"))
    icon = models.ImageField(upload_to='home/icons/', verbose_name=_("Rasmi"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "4. Counter"
        verbose_name_plural = "4. Counter"

class HomeLeaders(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Ism familiya"))
    position = models.CharField(max_length=255, verbose_name=_("Lavozimi"))
    image = models.ImageField(upload_to='home/leaders/', verbose_name=_("Rasmi"))

    content = models.TextField(verbose_name=_("Asosiy matn"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "5. Rahbariyat"
        verbose_name_plural = "5. Rahbariyat"

class HomePartners(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_("Sarlavha")
    )
    image = models.ImageField(
        upload_to='partners/',
        verbose_name=_("Rasm")
    )
    link = models.CharField(
        max_length=255,
        verbose_name=_("Havola")
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("6. Hamkorlar")
        verbose_name_plural = _("6. Hamkorlar")
