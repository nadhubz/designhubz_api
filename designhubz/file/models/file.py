from django.db import models
from django.contrib import admin


class FileManager(models.Manager):
    pass


class File(models.Model):
    user = models.ForeignKey('web.User', null=True, default=None, blank=True)
    folder = models.ForeignKey('Folder', null=True, default=None, blank=True)
    name = models.CharField(max_length=50)
    sort = models.IntegerField(default=0)

    objects = FileManager()

    class Meta:
        app_label = 'file'
        verbose_name = 'file'
        verbose_name_plural = 'files'
        ordering = ['sort', 'name']

    def __str__(self):
        return self.name


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'folder',
        'user',
        'sort'
    )
