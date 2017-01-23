from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('chat.urls')),
    url(r'^', include('project.urls')),
    url(r'^', include('web.urls')),
]

admin.site.site_header = 'designhubz'
admin.site.site_title = 'designhubz'
