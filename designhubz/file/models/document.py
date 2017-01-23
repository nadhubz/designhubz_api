from django.db import models
from django.contrib import admin


class DocumentManager(models.Manager):
    pass


class Document(models.Model):
    IMAGE = 'IMAGE'
    PDF = 'PDF'
    WORD = 'WORD'
    EXCEL = 'EXCEL'

    TYPE_CHOICES = (
        (IMAGE, 'image'),
        (PDF, 'pdf'),
        (WORD, 'word'),
        (EXCEL, 'excel')
    )

    file = models.ForeignKey('File')
    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES)

    objects = DocumentManager()

    class Meta:
        app_label = 'file'
        verbose_name = 'document'
        verbose_name_plural = 'documents'
        ordering = ['id']

    def __str__(self):
        return '{}: {}'.format(self.file.name, self.type)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        'file',
        'type'
    )
