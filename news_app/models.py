from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Sarlavha"))

    class Meta:
        verbose_name = _("1. Kategoriyalar")
        verbose_name_plural = _("1. Kategoriyalar")

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class NewsImage(models.Model):
    image = models.ImageField(upload_to='news_images/', verbose_name=_("Rasm"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))

    class Meta:
        verbose_name = _("3. Yangilik Rasmlari")
        verbose_name_plural = _("3. Yangilik Rasmlari")

    def __str__(self):
        return f"Rasm {self.id}"

class News(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='news', verbose_name=_("Kategoriya"))
    is_elon = models.BooleanField(verbose_name=_("Bu e'lon"), default=False)
    title = models.CharField(max_length=200, verbose_name=_("Sarlavha"))
    body = models.TextField(verbose_name=_("Matn"))

    image = models.ImageField(upload_to='news_images/', verbose_name=_("Asosiy rasm"))
    images = models.ManyToManyField(NewsImage, related_name='news', verbose_name=_("Rasmlar"), blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan vaqti"))

    class Meta:
        verbose_name = _("2. Yangiliklar")
        verbose_name_plural = _("2. Yangiliklar")
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.pk})

class NewsDetailText(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Sarlavha"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("4. Yangilik tugmacha matni")
        verbose_name_plural = _("4. Yangilik tugmacha matni")
