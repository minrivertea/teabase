from django.conf import settings
from django.conf.urls import patterns, include, url

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.contrib import admin
admin.autodiscover()

from teas.views import search

urlpatterns = patterns('',
    (r'^', include('teabase.teas.urls')),
    url(r'^search/$', search, name="search"),

    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
