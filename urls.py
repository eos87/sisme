from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from sisme.settings import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sisme.views.home'),
    url(r'^index/$', 'sisme.views.index'),
    url(r'^generales/$', 'sisme.fed.views.generales', name='generales'),
    url(r'^ajax/orgs/$', 'sisme.utils.get_orgs'),
    url(r'^xls/$', 'sisme.utils.save_as_xls'),
    url(r'^graph-params/$', 'sisme.utils.graph_params'),
    url(r'^view-graph/$', 'sisme.utils.view_graph'),
    url(r'^ajax/meses/$', 'sisme.utils.ajax_meses'),     
    url(r'^a/', include('sisme.contraparte.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

if DEBUG:
    urlpatterns += patterns('',
                (r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
                )