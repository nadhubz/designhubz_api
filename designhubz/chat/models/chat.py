from django.db import models
from django.contrib import admin


class ChatManager(models.Manager):
    pass


class Chat(models.Model):
    project = models.ForeignKey('project.Project')
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, default=None, blank=True)

    objects = ChatManager()

    class Meta:
        app_label = 'chat'
        verbose_name = 'chat'
        verbose_name_plural = 'chat'
        ordering = ['-updated_at']

    def __str__(self):
        return self.name


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = (
        'project',
        'name',
        'created_at',
        'updated_at'
    )
