from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','tmdps.views.index',name = 'index'),
    url(r'^DPS/','tmdps.views.DPS',name = 'DPS'),
    url(r'^admin/', include(admin.site.urls)),
)
