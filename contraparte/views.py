from django.shortcuts import render_to_response
from django.template.context import RequestContext
from forms import InfluenciaForm
from models import *
from sisme.fed.models import Tema

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
        
    return render_to_response('contraparte/acciones_impulsadas.html', RequestContext(request, locals()))
        
        
        
        
        
        
        