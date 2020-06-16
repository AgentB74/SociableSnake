from django.contrib import admin
from .models import Message, Dialog


# Register your models here.
# класс Inline позволяет включать модель в качестве подмодели в другую модель
class MessageInline(admin.TabularInline):
    model = Message
    raw_id_fields = ['dialog_id']


@admin.register(Dialog)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'recipient']
    list_filter = ['sender', 'recipient']
    inlines = [MessageInline]


@admin.register(Message)
class MessageTextAdmin(admin.ModelAdmin):
    list_display = ['id', 'dialog_id', 'created', 'updated']
    list_filter = ['id', 'dialog_id', 'created', 'updated']