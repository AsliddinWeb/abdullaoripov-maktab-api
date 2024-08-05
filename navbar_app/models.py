from django.db import models
from django.utils.translation import gettext_lazy as _

class NavType(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Sarlavha"))
    type = models.CharField(max_length=100, unique=True, verbose_name=_("Turi"))

    class Meta:
        verbose_name = _("Menyu Turi")
        verbose_name_plural = _("Menyu Turlari")

    def __str__(self):
        return self.title

class OneNavbar(models.Model):
    nav_type = models.ForeignKey(NavType, on_delete=models.PROTECT, related_name='one_navbars', verbose_name=_("Menyu Turi"))
    title = models.CharField(max_length=100, verbose_name=_("Sarlavha"))
    link = models.CharField(max_length=255, verbose_name=_("Havola"), default="#")
    is_submenu = models.BooleanField(default=False, verbose_name=_("Ichma-ich menyu"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Tartib"))

    class Meta:
        verbose_name = _("1-darajali menyu")
        verbose_name_plural = _("1-darajali menyular")
        ordering = ['order']

    def __str__(self):
        return self.title

class TwoNavbar(models.Model):
    nav_type = models.ForeignKey(NavType, on_delete=models.PROTECT, related_name='two_navbars', verbose_name=_("Menyu Turi"))
    one_navbar = models.ForeignKey('OneNavbar', on_delete=models.CASCADE, related_name='two_navbars', verbose_name=_("1-darajali menyu"))
    title = models.CharField(max_length=100, verbose_name=_("Sarlavha"))
    link = models.CharField(max_length=255, verbose_name=_("Havola"), default="#")
    is_submenu = models.BooleanField(default=False, verbose_name=_("Ichma-ich menyu"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Tartib"))

    class Meta:
        verbose_name = _("2-darajali menyu")
        verbose_name_plural = _("2-darajali menyular")
        ordering = ['order']

    def __str__(self):
        return self.title

class ThreeNavbar(models.Model):
    nav_type = models.ForeignKey(NavType, on_delete=models.PROTECT, related_name='three_navbars', verbose_name=_("Menyu Turi"))
    two_navbar = models.ForeignKey('TwoNavbar', on_delete=models.CASCADE, related_name='three_navbars', verbose_name=_("2-darajali menyu"))
    title = models.CharField(max_length=100, verbose_name=_("Sarlavha"))
    link = models.CharField(max_length=255, verbose_name=_("Havola"), default="#")
    is_submenu = models.BooleanField(default=False, verbose_name=_("Ichma-ich menyu"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Tartib"))

    class Meta:
        verbose_name = _("3-darajali menyu")
        verbose_name_plural = _("3-darajali menyular")
        ordering = ['order']

    def __str__(self):
        return self.title
