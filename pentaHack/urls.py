from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^kongfu/', include('kongfu.urls')),
)
