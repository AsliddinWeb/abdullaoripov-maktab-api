from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import TelegramBot, Message

@admin.register(TelegramBot)
class TelegramBotAdmin(ModelAdmin):
    list_display = ('title', 'token', 'admins')
    search_fields = ('title', )

@admin.register(Message)
class MessageAdmin(ModelAdmin):
    list_display = ('name', 'phone', 'is_view')
    search_fields = ('name', 'phone', 'message')
    list_filter = ('is_view',)
