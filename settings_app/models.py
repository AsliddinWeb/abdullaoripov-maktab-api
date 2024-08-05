from django.db import models
from django.utils.translation import gettext_lazy as _

class SeoSettings(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Sarlavha"))
    keywords = models.TextField(verbose_name=_("Kalit so'zlar"))
    description = models.TextField(verbose_name=_("Tavsif"))
    author = models.CharField(max_length=255, verbose_name=_("Muallif"))
    favicon = models.ImageField(upload_to='favicons/', verbose_name=_("Favicon"))
    robots = models.TextField(null=True, blank=True)
    site = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _("1. SEO Sozlamasi")
        verbose_name_plural = _("1. SEO Sozlamalari")

    def __str__(self):
        return self.title


class HeaderSettings(models.Model):
    test_message = models.CharField(max_length=255, verbose_name=_("Test rejimi xabarnomasi"))

    location_link = models.CharField(max_length=255, verbose_name=_("Joylashuv havolasi"))
    location = models.CharField(max_length=20, verbose_name=_("Joylashuv matni"))

    email_link = models.CharField(max_length=255, verbose_name=_("Email havolasi"))
    email = models.EmailField(max_length=255, verbose_name=_("Email"))

    logo = models.ImageField(upload_to='logos/', verbose_name=_("Logo"))
    logo_alt = models.CharField(max_length=255, verbose_name=_("Logo alt"))

    search_placeholder = models.CharField(max_length=100, verbose_name=_("Qidiruv matni"))

    class Meta:
        verbose_name = _("2. Header Sozlamalari")
        verbose_name_plural = _("2. Header Sozlamalari")

    def __str__(self):
        return f"Header Sozlamalari ({self.id})"


class FooterSettings(models.Model):
    footer_logo = models.ImageField(upload_to='footer_logos/', verbose_name=_("Footer logosi"))
    title = models.CharField(max_length=255, verbose_name=_("Sarlavha"))

    location = models.CharField(max_length=255, verbose_name=_("Joylashuv"))
    phone = models.CharField(max_length=255, verbose_name=_("Telefon raqam"))

    body = models.TextField(verbose_name=_("Matn"))
    copyright = models.CharField(max_length=255, verbose_name=_("Mualliflik huquqi"))

    note = models.CharField(max_length=255, verbose_name=_("Eslatma"))

    class Meta:
        verbose_name = _("3. Footer Sozlamasi")
        verbose_name_plural = _("3. Footer Sozlamalari")

    def __str__(self):
        return f"Footer Settings ({self.id})"


class FooterLinkCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Sarlavha"))

    class Meta:
        verbose_name = _("4. Footer Havola Kategoriyasi")
        verbose_name_plural = _("4. Footer Havola Kategoriyalari")

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    category = models.ForeignKey(FooterLinkCategory, on_delete=models.CASCADE, related_name='links', verbose_name=_("Kategoriya"))
    title = models.CharField(max_length=100, verbose_name=_("Sarlavha"))
    link = models.CharField(max_length=255, verbose_name=_("Havola"))

    class Meta:
        verbose_name = _("5. Footer Havolasi")
        verbose_name_plural = _("5. Footer Havolalari")

    def __str__(self):
        return self.title


class SocialSettings(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Sarlavha'))
    i_class = models.CharField(max_length=255, verbose_name=_('Ikonka klassi'))
    link = models.CharField(max_length=255, verbose_name=_('Havola'))

    class Meta:
        verbose_name = _('7. Ijtimoiy tarmoq sozlamasi')
        verbose_name_plural = _('7. Ijtimoiy tarmoq sozlamalari')

    def __str__(self):
        return self.title


class MoreTitles(models.Model):
    home = models.CharField(max_length=255, verbose_name=_("Bosh sahifa"))
    related_news = models.CharField(max_length=255, verbose_name=_("O'xshash yangiliklar"), null=True, blank=True)
    news_page = models.CharField(max_length=255, verbose_name=_("Yangiliklar sahifasi"), null=True, blank=True)

    search_title = models.CharField(max_length=255, verbose_name=_("Qidiruv sarlavhasi"), null=True, blank=True)
    news_category_title = models.CharField(max_length=255, verbose_name=_("Yangiliklar kategoriya sarlavhasi"), null=True, blank=True)
    share = models.CharField(max_length=255, verbose_name=_("Ijtimoiy tarmoqlarga uzatish matni"), null=True, blank=True)
    empty_news = models.TextField(verbose_name=_("Yangiliklar yo'q"), null=True, blank=True)

    class Meta:
        verbose_name = "8. Ichki matnlar"
        verbose_name_plural = "8. Ichki matnlar"

class ErrorTexts(models.Model):
    error_404_title = models.CharField(max_length=255, verbose_name=_("404 Sarlavhasi"))
    error_404_body = models.TextField(verbose_name=_("404 Matni"))

    error_500_title = models.CharField(max_length=255, verbose_name=_("500 Sarlavhasi"))
    error_500_body = models.TextField(verbose_name=_("500 Matni"))

    def __str__(self):
        return self.error_404_title

    class Meta:
        verbose_name = "8. Xatolik sahifasi matnlari"
        verbose_name_plural = "8. Xatolik sahifasi matnlari"
