from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from sisme.settings import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sisme.views.index'),
    url(r'^generales/$', 'sisme.fed.views.generales', name='generales'),
    url(r'^ajax/orgs/$', 'sisme.utils.get_orgs'),
    url(r'^xls/$', 'sisme.utils.save_as_xls'),     
    url(r'^a/', include('sisme.contraparte.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()