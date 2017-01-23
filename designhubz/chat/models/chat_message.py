"""
Implement Redis subscriber here.
"""

from django.db import models
from django.contrib import admin


class ChatMessageManager(models.Manager):
    pass


class ChatMessage(models.Model):
    chat = models.ForeignKey('Chat')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_edited = models.BooleanField(default=False)

    objects = ChatMessageManager()

    class Meta:
        app_label = 'chat'
        verbose_name = 'chat message'
        verbose_name_plural = 'chat messages'
        ordering = ['-created_at']

    def __str__(self):
        return self.message[:30]


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = (
        'chat',
        'message',
        'created_at',
        'is_edited'
    )
