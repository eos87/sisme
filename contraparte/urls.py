from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('sisme.contraparte.views',
    (r'^indicadores/$', 'indicadores'),
    (r'^impulsando-politicas-publicas/$', 'impulsando_politicas_publicas'),

#    (r'^lideres/$', direct_to_template, {'template': 'monitoreo/lideres.html'}),
#    (r'^lideres/(?P<vista>[-\w]+)/$', 'trocaire.encuesta.views._get_vista_lideres'),
    
)