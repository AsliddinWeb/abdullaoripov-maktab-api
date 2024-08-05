from django.contrib import admin

# Unfold admin
from unfold.admin import ModelAdmin

from .models import HomeWelcome, HomeAbout, Counter, HomeLeaders, HomePartners

@admin.register(HomeWelcome)
class HomeWelcomeAdmin(ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )

@admin.register(HomeAbout)
class HomeAboutAdmin(ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', 'cap_title', )

@admin.register(Counter)
class CounterAdmin(ModelAdmin):
    list_display = ('title', 'value')
    search_fields = ('title', 'value')

@admin.register(HomeLeaders)
class HomeLeadersAdmin(ModelAdmin):
    list_display = ('name', 'position')
    search_fields = ('name', 'position', )

@admin.register(HomePartners)
class HomePartnersAdmin(ModelAdmin):
    list_display = ('title', 'link')
    search_fields = ('title', 'link')
