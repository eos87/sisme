# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db.models import Sum
from forms import InfluenciaForm
from models import *
from sisme.fed.models import *

def indicadores(request):
    if request.method == 'POST':
        form = InfluenciaForm(request.POST)
        if form.is_valid():
            request.session['modalidad'] = form.cleaned_data['modalidad']
            request.session['organizacion'] = form.cleaned_data['organizacion']
            request.session['resultado'] = form.cleaned_data['resultado']
            request.session['meses'] = form.cleaned_data['meses']
            request.session['anio'] = form.cleaned_data['anio']            
            centinela = 1            
    else:
        form = InfluenciaForm()
        centinela = 0
    return render_to_response('contraparte/indicadores.html', RequestContext(request, locals()))


def _query_set_filtrado(request):
    params = {}

    if request.session['modalidad']:
        params['proyecto__modalidad__in'] = request.session['modalidad']
        
    if request.session['organizacion']:
        params['organizacion__id__in'] = request.session['organizacion']
        
    if request.session['resultado']:
        params['proyecto__resultados__id__in'] = request.session['resultado']
        
    if request.session['meses']:
        params['mes__in'] = request.session['meses']
    
    if request.session['anio']:
        params['anio'] = request.session['anio']    
        
    return Informe.objects.filter(** params)

#------------- Resultado 1.1 ------------------------
def acciones_impulsadas(request):
    tabla_por_tipo = {}
    temas = Tema.objects.all()
    informes = _query_set_filtrado(request)
    
    #Utilizando dict comprehension, soportado solo por python2.7+
    for op in ACCIONES:
        tabla_por_tipo[op[1]] = {tema.nombre: AccionImpulsada.objects.filter(informe__in=informes, \
                                                                      tema=tema, \
                                                                      tipo_accion=op[0]).count() for tema in temas}
    tabla_por_ambito = {}
    for op in AMBITO:
        tabla_por_ambito[op[1]] = {tema.nombre: AccionImpulsada.objects.filter(informe__in=informes, \
                                                                      tema=tema, \
                                                                      ambito=op[0]).count() for tema in temas}
    tabla_estado_accion = {}
    for op in ACCION:
        tabla_estado_accion[op[1]] = {tema.nombre: AccionImplementada.objects.filter(informe__in=informes, \
                                                                      tema=tema, \
                                                                      accion=op[0]).count() for tema in temas}
    tabla_estado_accion_2 = {}
    for op in ACCION:
        tabla_estado_accion_2[op[1]] = {estado[1]: AccionImplementada.objects.filter(informe__in=informes, \
                                                                                     estado=estado[0], \
                                                                                     accion=op[0]).count() for estado in ESTADO_ACCION}
        
    return render_to_response('contraparte/acciones_impulsadas.html', RequestContext(request, locals()))
        
def participacion_comisiones(request):
    informes = _query_set_filtrado(request)
    tabla_tipo_comisiones = {}
    for org in informes.values_list('organizacion__nombre_corto', flat=True):
        tabla_tipo_comisiones[org] = {comision[1]: ParticipacionComision.objects.filter(informe__in=informes.filter(organizacion__nombre_corto=org),
                                                                                        comision=comision[0]).count() for comision in COMISION_CHOICE}
    
    tabla_ambito_comisiones = {}
    for ambito in AMBITO:
        tabla_ambito_comisiones[ambito[1]] = {comision[1]: ParticipacionComision.objects.filter(informe__in=informes, \
                                                                                                ambito=ambito[0], \
                                                                                                comision=comision[0]).count() \
                                              for comision in COMISION_CHOICE}
    tabla_comision_estado = {}
    for comision in COMISION_CHOICE:
        tabla_comision_estado[comision[1]] = {estado[1]: ParticipacionComision.objects.filter(informe__in=informes, \
                                                                                              comision=comision[0], \
                                                                                              estado=estado[0]).count() \
                                              for estado in ESTADO_ACCION}
    
    return render_to_response('contraparte/participacion_comisiones.html', RequestContext(request, locals()))

def defensa_ddssrr(request):
    temas = Tema.objects.all()
    titulo = u'Acciones para defensa de los DDSSRR'
    informes = _query_set_filtrado(request)
    
    tabla_tipo_accion = {}    
    for accion in ACCIONES2:
        tabla_tipo_accion[accion[1]] = {tema.nombre: AgendaPublica.objects.filter(informe__in=informes, \
                                                                                  tipo_accion=accion[0], \
                                                                                  tema=tema).count() for tema in temas}   
    
    tabla_ambito_accion = {}
    for ambito in AMBITO:
        tabla_ambito_accion[ambito[1]] = {accion[1]: AgendaPublica.objects.filter(informe__in=informes, \
                                                                                  ambito=ambito[0], \
                                                                                  tipo_accion=accion[0]).count() for accion in ACCIONES2}                         
    
    return render_to_response('contraparte/defensa_ddssrr.html', RequestContext(request, locals()))

#--------------------- Resultado 1.2 --------------------------------
def acciones_impulsadas_demandas(request):
    temas = Tema.objects.all()
    informes = _query_set_filtrado(request)
    
    tabla_acciones_publicas = {}
    for org in informes.values_list('organizacion__nombre_corto', flat=True):
        tabla_acciones_publicas[org] = {poblacion[1]: DemandaJusticia.objects.filter(informe__in=informes.filter(organizacion__nombre_corto=org), \
                                                                                    poblacion_discriminada=poblacion[0]).count() for poblacion in POBLACION}
    
    tabla_tipo_acciones = {}
    for accion in ACCION_DEMANDA:
        tabla_tipo_acciones[accion[1]] = {poblacion[1]: DemandaJusticia.objects.filter(informe__in=informes, 
                                                                                       accion=accion[0],
                                                                                       poblacion_discriminada=poblacion[0]).count() \
                                          for poblacion in POBLACION}
        
    tabla_denuncias = {}
    for poblacion in TIPO_POBLACION:
        tabla_denuncias[poblacion[1]] = {situacion[1]: Denuncia.objects.filter(informe__in=informes, \
                                                                               tipo_poblacion=poblacion[0], \
                                                                               situacion=situacion[0]).count() for situacion in DENUNCIAS}
    
    return render_to_response('contraparte/acciones_impulsadas_demandas.html', RequestContext(request, locals()))

#----------------------- Resultado 2.1 --------------------------------------
def acciones_reflexion(request):
    informes = _query_set_filtrado(request)
    temas = Tema.objects.all()
    
    tabla_reflexion = {}
    for accion in ACCION_POSEE_INFO:
        tabla_reflexion[accion[1]] = {tema.nombre: PoseenInfo.objects.filter(informe__in=informes, 
                                                                             tipo_accion=accion[0], \
                                                                             tema=tema).count() for tema in temas}
    
    return render_to_response('contraparte/acciones_reflexion.html', RequestContext(request, locals()))

def involucramiento_poblacion(request):    
    informes = _query_set_filtrado(request)
    
    titulos = {'mujeres': 'Participantes mujeres', 'hombres': 'Participantes hombres'}
        
    dicc = {'Participantes mujeres': {u'Niñas': 'muj_ninas',
                                      u'Adolescentes': 'muj_adols',
                                      u'Jóvenes': 'muj_jovenes',
                                      u'Adultas': 'muj_adultas'},
            'Participantes hombres': {u'Niños': 'hom_ninos',
                                      u'Adolescentes': 'hom_adols',
                                      u'Jóvenes': 'hom_jovenes',
                                      u'Adultos': 'hom_adultos'},
            }    
    
    check_none = lambda x: x if x else 0
    
    resultados = {}
    for grupo, campos in dicc.items():
        resultados[grupo] = {}
        for accion in ACCION_POSEE_INFO:
            query = PoseenInfo.objects.filter(informe__in=informes, tipo_accion=accion[0])            
            resultados[grupo][accion[1]] = {key: check_none(query.aggregate(campo_sum=Sum(field))['campo_sum']) for key, field in campos.items()}
    
    return render_to_response('contraparte/involucramiento-poblacion.html', RequestContext(request, locals()))



        
    
    
    
    
    
    
        
        
        
        
        