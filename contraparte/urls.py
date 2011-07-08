from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('sisme.contraparte.views',
    (r'^indicadores/$', 'indicadores'),
    
    #------------- Indicadores de resultado 1.1 ------------------------    
    (r'^impulsando-politicas-publicas/$', 'impulsando_politicas_publicas'),    
    
    #------------- Indicadores de resultado 1.2 ------------------------    
    (r'^demandando-justicia/$', 'demandando_justicia'),
    
    #------------- Indicadores de resultado 2.1 ------------------------
    (r'^involucramiento-poblacion/$', 'involucramiento_poblacion'),
    (r'^acciones-reflexion/$', 'acciones_reflexion'),
    
)