# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.db.models import Sum
from forms import InfluenciaForm
from models import *
from sisme.fed.models import *
import json

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

def reducir_lista(lista):    
    meh = []
    for foo in lista:
        if not foo in meh:
            meh.append(foo)
    return meh

def influencia(request):
    if request.method == 'POST':
        form = InfluenciaForm(request.POST)
        if form.is_valid():
            request.session['modalidad'] = form.cleaned_data['modalidad']
            request.session['organizacion'] = form.cleaned_data['organizacion']
            request.session['resultado'] = form.cleaned_data['resultado']
            request.session['meses'] = form.cleaned_data['meses']
            request.session['anio'] = form.cleaned_data['anio'] 
                                
            dicc = {}            
            query = _query_set_filtrado(request)
            if query.count() != 0:
                centinela = 1
            else:
                centinela = 2                
            for municipio in reducir_lista(query.values('proyecto__tematrabajo__municipio__nombre', 
                                          'proyecto__tematrabajo__municipio__latitud',
                                          'proyecto__tematrabajo__municipio__longitud',
                                          'proyecto__tematrabajo__municipio__id')):
                dicc[municipio['proyecto__tematrabajo__municipio__id']] \
                = {'lat': float(municipio['proyecto__tematrabajo__municipio__latitud']),
                   'lng': float(municipio['proyecto__tematrabajo__municipio__longitud']),
                   'name': municipio['proyecto__tematrabajo__municipio__nombre'], 
                   'proys': []
                   }
            
            for obj in query:
                for tema in obj.proyecto.tematrabajo_set.all():
                    for muni in tema.municipio.all():
                        proyecto = '<b>[%s]</b> %s' % (obj.organizacion.nombre_corto, obj.proyecto.nombre)
                        if not proyecto in dicc[muni.id]['proys']:
                            dicc[muni.id]['proys'].append(proyecto)
            markers = json.dumps(dicc)             
    else:
        form = InfluenciaForm()
        centinela = 0
        
    return render_to_response('contraparte/influencia.html', RequestContext(request, locals()))

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
def impulsando_politicas_publicas(request):
    tabla_por_tipo = {}
    temas = Tema.objects.all()
    informes = _query_set_filtrado(request)
    
    #Utilizando dict comprehension, soportado solo por python2.7+
    for op in ACCIONES:
        tabla_por_tipo[op[1]] = {tema.nombre: AccionImpulsada.objects.filter(informe__in=informes,
                                                                      tema=tema,
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
    
    #------ Participacion en comisiones -----------------------
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
        
    return render_to_response('contraparte/impulsando_politicas_publicas.html', RequestContext(request, locals()))        

#--------------------- Resultado 1.2 --------------------------------
def demandando_justicia(request):
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
    
    return render_to_response('contraparte/demandando_justicia.html', RequestContext(request, locals()))

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

dicc = {1: {'Participantes mujeres': {u'Niñas': 'muj_ninas',
                                           u'Adolescentes': 'muj_adols',
                                           u'Jóvenes': 'muj_jovenes',
                                           u'Adultas': 'muj_adultas'}},
            2: {'Participantes hombres': {u'Niños': 'hom_ninos',
                                           u'Adolescentes': 'hom_adols',
                                           u'Jóvenes': 'hom_jovenes',
                                           u'Adultos': 'hom_adultos'}},
            3: {'Participantes LGBT': {u'Trans': 'lgbt_trans',
                                       u'Lesbianas': 'lgbt_lesbi',
                                       u'Gay': 'lgbt_gay',
                                       u'HSH': 'lgbt_hsh'}},
            4: {'Mujeres discapacitadas': {u'Niñas': 'muj_disca_ninas',
                                           u'Adolescentes': 'muj_disca_adols',
                                           u'Jóvenes': 'muj_disca_jovenes',
                                           u'Adultas': 'muj_disca_adultas'},
                'Hombres discapacitados': {u'Niños': 'hom_disca_ninos',
                                           u'Adolescentes': 'hom_disca_adols',
                                           u'Jóvenes': 'hom_disca_jovenes',
                                           u'Adultos': 'hom_disca_adultos'}},
            5: {u'Mujeres población étnicas': {u'Niñas': 'muj_etnia_ninas',
                                    u'Adolescentes': 'muj_etnia_adols',
                                    u'Jóvenes': 'muj_etnia_jovenes',
                                    u'Adultas': 'muj_etnia_adultas'},
                u'Hombres población étnicos': {u'Niños': 'hom_etnia_ninos',
                                    u'Adolescentes': 'hom_etnia_adols',
                                    u'Jóvenes': 'hom_etnia_jovenes',
                                    u'Adultos': 'hom_etnia_adultos'}},
            6: {u'Mujeres con VIH': {u'Niñas': 'muj_vih_ninas',
                                    u'Adolescentes': 'muj_vih_adols',
                                    u'Jóvenes': 'muj_vih_jovenes',
                                    u'Adultas': 'muj_vih_adultas'},
                u'Hombres con VIH': {u'Niños': 'hom_vih_ninos',
                                    u'Adolescentes': 'hom_vih_adols',
                                    u'Jóvenes': 'hom_vih_jovenes',
                                    u'Adultos': 'hom_vih_adultos'}}            
            }

check_none = lambda x: x if x else 0

def involucramiento_poblacion(request):    
    informes = _query_set_filtrado(request)
    
    resultados = {}    
    for grupo, valores in dicc.items():
        resultados[grupo] = {}
        for k, campos in valores.items():            
            resultados[grupo][k] = {}            
            for accion in ACCION_POSEE_INFO:
                query = PoseenInfo.objects.filter(informe__in=informes, tipo_accion=accion[0])
                resultados[grupo][k][accion[1]] = {key: check_none(query.aggregate(campo_sum=Sum(field))['campo_sum']) for key, field in campos.items()}
                
    resultados_2 = {}
    for grupo, valores in dicc.items():
        resultados_2[grupo] = {}
        for k, campos in valores.items():            
            resultados_2[grupo][k] = {}            
            for accion in ACCION_POSEE_INFO:
                query = RecibenInfo.objects.filter(informe__in=informes, tipo_accion=accion[0])
                resultados_2[grupo][k][accion[1]] = {key: check_none(query.aggregate(campo_sum=Sum(field))['campo_sum']) for key, field in campos.items()}
    
    return render_to_response('contraparte/involucramiento-poblacion.html', RequestContext(request, locals()))

def prevencion_violencia(request):
    informes = _query_set_filtrado(request)
    resultados = {}    
    for grupo, valores in dicc.items():
        resultados[grupo] = {}
        for k, campos in valores.items():            
            resultados[grupo][k] = {}            
            for accion in ACCION_PREVENCION:
                query = PrevencionVBG.objects.filter(informe__in=informes, tipo_accion=accion[0])
                resultados[grupo][k][accion[1]] = {key: check_none(query.aggregate(campo_sum=Sum(field))['campo_sum']) for key, field in campos.items()}
                
    resultados_2 = {}
    for grupo, valores in dicc.items():
        resultados_2[grupo] = {}
        for k, campos in valores.items():            
            resultados_2[grupo][k] = {}            
            for accion in ACCION_PREVENCION:
                query = MasculinidadLibre.objects.filter(informe__in=informes, tipo_accion=accion[0])
                resultados_2[grupo][k][accion[1]] = {key: check_none(query.aggregate(campo_sum=Sum(field))['campo_sum']) for key, field in campos.items()}
                
    return render_to_response('contraparte/prevencion_violencia.html', RequestContext(request, locals()))

def acceso_a_servicios(request):
    informes = _query_set_filtrado(request)
    tabla_casos_atendidos = {}
    organizaciones = [informe.organizacion for informe in informes]
    
    for organizacion in organizaciones:
        query = informes.filter(organizacion=organizacion)
        tabla_casos_atendidos[organizacion.nombre_corto] = {tipo[1]: check_none(CasoAtendido.objects.filter(informe__in=query,
                                                                             tipo_caso=tipo[0], situacion_caso=2).aggregate(campo_sum=Sum('cantidad'))['campo_sum']) + \
                                                            check_none(CasoAtendido.objects.filter(informe__in=query,
                                                                             tipo_caso=tipo[0], situacion_caso=3).aggregate(campo_sum=Sum('cantidad'))['campo_sum']) 
                                                            for tipo in TIPOS_CASOS}
    
    SITUACION_C = ((2, u'Nuevo'), (3, 'En seguimiento'), (4, u'En abandono'), (5, u'Con diagnóstico favorable'))
    tabla_estado_casos = {}
    for tipo in TIPOS_CASOS:
        tabla_estado_casos[tipo[1]] = {situacion[0]: check_none(CasoAtendido.objects.filter(informe__in=informes,
                                                                                 situacion_caso = situacion[0], 
                                                                                 tipo_caso=tipo[0]).aggregate(campo_sum=Sum('cantidad'))['campo_sum']) \
                                       for situacion in SITUACION_C}
        #sacar total para nuevos y en seguimiento
        tabla_estado_casos[tipo[1]]['total'] = tabla_estado_casos[tipo[1]][2] + tabla_estado_casos[tipo[1]][3]
        
    tabla_denuncias = {}
    denuncia_query = DenunciaInterpuesta.objects.filter(informe__in=informes)
    for tipo in TIPO_DENUNCIA:
        tabla_denuncias[tipo[1]] = {instancia[1]: check_none(denuncia_query.filter(tipo_denuncia = tipo[0], 
                                                                                   instancia_administra=instancia[0]).count()) \
                                    for instancia in INSTANCIA_ADMINISTRA}
        
    tabla_estado_denuncias = {}
    for instancia in INSTANCIA_ADMINISTRA:
        tabla_estado_denuncias[instancia[1]] = {situacion[1]: check_none(denuncia_query.filter(situacion_denuncia = situacion[0],
                                                                                                instancia_administra=instancia[0]).count()) \
                                    for situacion in SITUACION_DENUNCIA}
    
    tabla_albergues = {}    
    for org in ORGANIZACION_CHOICE:
        query = AtencionMujer.objects.filter(informe__in=informes, organizacion=org[0])        
        tabla_albergues[org[1]] = {tipo[0]: query.filter(tipo_poblacion=tipo[0]).count() for tipo in TIPO_POBLACION_ATENCION}
        
        #sacar total para cada llave
        total = sum(tabla_albergues[org[1]].values())
        #calcular lo que tienen proyecto de vida
        cantidad = query.filter(plan_vida=1).count()
        
        tabla_albergues[org[1]]['plan'] = cantidad
        tabla_albergues[org[1]]['porcentaje'] = get_porcentaje(total, cantidad)
        tabla_albergues[org[1]]['total'] = total
        
    REF_CONTRA = ((1, u'Referencias'), (2, u'Contrareferencias'))
    tabla_ref_contra = {}
    for op in REF_CONTRA:
        tabla_ref_contra[op[1]] = {instancia[1]: ReferenciaContraReferencia.objects.filter(informe__in=informes,
                                                                             tipo_referencia=op[0],
                                                                             instancia=instancia[0]).count() \
                                   for instancia in INSTANCIA_PUBLICA}
    
    return render_to_response('contraparte/acceso_a_servicios.html', RequestContext(request, locals()))
    
def capacidad_tecnica(request):
    informes = _query_set_filtrado(request)
    tabla_cap_admitiva = {}
    for op in A_TRAVES:
        tabla_cap_admitiva[op[1]] = CapacidadAdmitiva.objects.filter(informe__in=informes, atraves=op[0], ha_mejorado=1).count()
        
    tabla_medir_reportar = {}
    for op in MANERA:
        tabla_medir_reportar[op[1]] = MedirReportar.objects.filter(informe__in=informes, manera=op[0], ha_mejorado=1).count()
        
    tabla_plan = {}
    for op in MANERA_PLAN:
        tabla_plan[op[1]] = PlanEstrategico.objects.filter(informe__in=informes, manera=op[0], utiliza_plan=1).count()
    
    return render_to_response('contraparte/capacidad_tecnica.html', RequestContext(request, locals()))

def get_porcentaje(total, cantidad):
    '''Metodo para calcular el porcentaje de una cantidad sobre un total'''
    if total == None or cantidad == None or total == 0:
        x = 0
    else:
        x = (cantidad * 100) / total
    return x
    
def organizacion_detail(request, id):
    org = get_object_or_404(Organizacion, id=id)
    
    return render_to_response('contraparte/organizacion_detail.html', RequestContext(request, locals()))
    
        
        
        
        
        