from django.db import models
from django.contrib import admin
from web.models import ActiveModel, ActiveManager


class ProjectManager(ActiveManager):
    def create_project(self, owner_id, name):
        p = self.model(owner_id=owner_id, name=name)
        p.save()
        return p


class Project(ActiveModel):
    ACTIVE = 'ACTIVE'
    COMPLETED = 'COMPLETED'
    ON_HOLD = 'ON_HOLD'
    CANCELLED = 'CANCELLED'
    NO_STATUS = 'NO_STATUS'

    STATUS_CHOICES = (
        (ACTIVE, 'active'),
        (COMPLETED, 'completed'),
        (ON_HOLD, 'on hold'),
        (CANCELLED, 'cancelled'),
        (NO_STATUS, 'no status'),
    )

    owner = models.ForeignKey('web.User')
    users = models.ManyToManyField(
        'web.User', related_name='projects')
    name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default=NO_STATUS)
    is_starred = models.BooleanField(default=False)
    sort = models.IntegerField(default=0)

    objects = ProjectManager()

    class Meta:
        app_label = 'project'
        verbose_name = 'project'
        verbose_name_plural = 'projects'
        ordering = ['sort']

    def __str__(self):
        return self.name


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'status',
        'is_starred',
        'sort'
    )
