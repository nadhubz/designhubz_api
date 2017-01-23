from mptt.models import MPTTModel, TreeForeignKey
from django_mptt_admin.admin import DjangoMpttAdmin
from django.db import models
from django.contrib import admin


class FolderManager(models.Manager):
    pass


class Folder(MPTTModel):
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        db_index=True,
        verbose_name='parent')
    name = models.CharField(max_length=50)
    sort = models.IntegerField(default=0)

    objects = FolderManager()

    class Meta:
        app_label = 'file'
        verbose_name = 'folder'
        verbose_name_plural = 'folders'
        ordering = ['sort', 'name']

    def __str__(self):
        return self.name


@admin.register(Folder)
class FolderAdmin(DjangoMpttAdmin):
    list_display = (
        'name',
        'parent',
        'sort'
    )
