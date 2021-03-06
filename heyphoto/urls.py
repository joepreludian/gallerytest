from django.conf.urls import patterns, include, url
from heyphoto import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r"^admin/", include(admin.site.urls)),
                       url(r'^', include('gallery.urls')))

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
