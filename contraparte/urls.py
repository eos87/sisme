from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('sisme.contraparte.views',
    (r'^indicadores/$', 'indicadores'),
    
    #------------- Indicadores de resultado 1.1 ------------------------
    (r'^impulsando-politicas-publicas/$', direct_to_template, {'template': 'contraparte/impulsando_politicas_publicas.html'}),
    (r'^acciones-impulsadas/$', 'acciones_impulsadas'),
    (r'^participacion-comisiones/$', 'participacion_comisiones'),
    (r'^defensa-ddssrr/$', 'defensa_ddssrr'), 
    
    #------------- Indicadores de resultado 1.2 ------------------------
    (r'^demandando-justicia/$', direct_to_template, {'template': 'contraparte/demandando_justicia.html'}),
    (r'^acciones-impulsadas-demandas/$', 'acciones_impulsadas_demandas'),
    
    #------------- Indicadores de resultado 2.1 ------------------------
    (r'^involucramiento-poblacion/$', 'involucramiento_poblacion'),
    (r'^acciones-reflexion/$', 'acciones_reflexion'),
    
)