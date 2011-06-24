from django.conf.urls.defaults import patterns, include, url
from sisme.settings import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^generales/$', 'sisme.fed.views.generales', name='generales'),    
    # url(r'^sisme/', include('sisme.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if DEBUG:
    urlpatterns += patterns('',
                            (r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),
                           )