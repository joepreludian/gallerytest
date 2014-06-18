from django.conf.urls import patterns, url

urlpatterns = patterns('gallery.views',
                       url(r'^$', 'gallery'),
                       url(r'^gallery/(?P<gallery_id>\d+)$', 'gallery_detail'))
