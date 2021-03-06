from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User
from .forms import UserCreationForm, UserChangeForm
from web import views

admin.site.unregister(Group)


class PopupMixin:
    def get_popup(self, url, name, width, height):
        opt = 'left=300, top=200, resizable=0, location=0, scrollbars=0,'
        opt += 'width={}, height={}'.format(width, height)
        popup = 'window.open("{}", "{}", "{}")'.format(url, name, opt)
        return popup


@admin.register(User)
class MyUserAdmin(PopupMixin, UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            'Info',
            {'fields':
                (
                    'first_name',
                    'last_name',
                    'email',
                    'is_confirmed',
                    'is_active')}
        ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2'
            )}),
    )

    empty_value_display = ''
    list_display = (
        'id',
        'email',
        'type',
        'first_name',
        'is_active',
        'is_admin'
    )
    list_filter = ('type',)
    list_display_links = ('id',)
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('email',)
    filter_horizontal = ()


def get_admin_urls(urls):
    def get_urls():
        my_urls = []

        l = [
        ]

        for model in l:
            for path, view_name in model.get_admin_urls():
                v = getattr(views, view_name)
                ptn = url(path, admin.site.admin_view(v))
                my_urls.append(ptn)
        return my_urls + urls
    return get_urls
admin_urls = get_admin_urls(admin.site.get_urls())
admin.site.get_urls = admin_urls
