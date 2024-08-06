from django.db import models
from django.utils.translation import gettext_lazy as _


class InfoImages(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Rasm nomi"))
    image = models.ImageField(upload_to='schoolinfo_app/', verbose_name=_("Rasm"))

    class Meta:
        verbose_name = "Maktab haqida rasmlar"
        verbose_name_plural = "Maktab haqida rasmlar"


class SchoolInfo(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Maktab nomi"))
    address = models.CharField(max_length=255, verbose_name=_("Manzili"))

    main_image = models.ImageField(upload_to='schoolinfo_app/', verbose_name=_("Asosiy rasm"))
    content = models.TextField(verbose_name=_("Asosiy matn"))

    images = models.ManyToManyField(InfoImages, verbose_name=_("Rasmlar"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan vaqti"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Maktab haqida"
        verbose_name_plural = "Maktab haqida"

class SchoolLeaders(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Ism familiya"))
    image = models.ImageField(upload_to='schoolinfo_app/', verbose_name=_("Rasmi"))
    position = models.CharField(max_length=255, verbose_name=_("Lavozimi"))

    phone = models.CharField(max_length=255, verbose_name=_("Telefon raqami"))
    education = models.CharField(max_length=255, verbose_name=_("Ta'lim"))
    email = models.CharField(max_length=255, verbose_name=_("Email"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Rahbariyat"
        verbose_name_plural = "Rahbariyat"

class Teachers(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Ism familiya"))
    image = models.ImageField(upload_to='schoolinfo_app/', verbose_name=_("Rasmi"))
    subject = models.CharField(max_length=255, verbose_name=_("Fan"))

    phone = models.CharField(max_length=255, verbose_name=_("Telefon raqami"))
    education = models.CharField(max_length=255, verbose_name=_("Ta'lim"))
    email = models.CharField(max_length=255, verbose_name=_("Email"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "O'qituvchilar"
        verbose_name_plural = "O'qituvchilar"

class EducationSystem(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Nomi"))
    main_image = models.ImageField(upload_to='schoolinfo_app/', verbose_name=_("Asosiy rasm"))

    content = models.TextField(verbose_name=_("Asosiy matn"))

    images = models.ManyToManyField(InfoImages, verbose_name=_("Rasmlar"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan vaqti"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ta'lim tizimi"
        verbose_name_plural = "Ta'lim tizimi"

class Gallery(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Rasm nomi"))
    image = models.ImageField(upload_to='schoolinfo_app/', verbose_name=_("Rasm"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan vaqti"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Galereya"
        verbose_name_plural = "Galereya"

class ApplyInfo(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Nomi"))
    image = models.ImageField(upload_to='schoolinfo_app/', verbose_name=_("Aossiy rasm"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan vaqti"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Qabul haqida"
        verbose_name_plural = "Qabul haqida"
