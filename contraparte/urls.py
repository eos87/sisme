from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('sisme.contraparte.views',
    (r'^indicadores/$', 'indicadores'),
    (r'^impulsando-politicas-publicas/$', direct_to_template, {'template': 'contraparte/impulsando_politicas_publicas.html'}),    
    #------------- Indicadores de resultado 1.1 ------------------------
    (r'^acciones-impulsadas/$', 'acciones_impulsadas'),
    
)