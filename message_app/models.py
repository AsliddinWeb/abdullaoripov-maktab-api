from django.db import models
from django.utils.translation import gettext_lazy as _


class TelegramBot(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Telegram Bot Sozlamalari"))
    token = models.TextField(verbose_name=_("Token"))
    admins = models.CharField(max_length=255, verbose_name=_("Admin ID lari"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("1. Telegram bot sozlamalari")
        verbose_name_plural = _("1. Telegram bot sozlamalari")

class Message(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Ism")
    )
    phone = models.CharField(
        max_length=255,
        verbose_name=_("Telefon")
    )
    message = models.TextField(
        verbose_name=_("Xabar")
    )
    is_view = models.BooleanField(
        default=False,
        verbose_name=_("Ko'rilganmi?")
    )

    class Meta:
        verbose_name = _("2. Xabarlar")
        verbose_name_plural = _("2. Xabarlar")

    def __str__(self):
        return f"{self.name} - {self.phone}"
