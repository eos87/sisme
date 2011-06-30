from django.shortcuts import render_to_response
from django.template.context import RequestContext
from forms import InfluenciaForm
from models import *

def indicadores(request):
    if request.method == 'POST':
        form = InfluenciaForm(request.POST)
        if form.is_valid():
            request.session['modalidad'] = form.cleaned_data['modalidad']
            request.session['organizacion'] = form.cleaned_data['organizacion']
            request.session['resultado'] = form.cleaned_data['resultado']
            request.session['mes_inicio'] = form.cleaned_data['mes_inicio']
            request.session['anio_inicio'] = form.cleaned_data['anio_inicio']
            request.session['mes_fin'] = form.cleaned_data['mes_fin']
            request.session['anio_fin'] = form.cleaned_data['anio_fin']
            centinela = 1
            informes = _query_set_filtrado(request)
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
        
    if request.session['mes_inicio']:
        params['mes_desde'] = request.session['mes_inicio']
    
    if request.session['anio_inicio']:
        params['anio_desde'] = request.session['anio_inicio']
    
    if request.session['mes_fin']:
        params['mes_hasta'] = request.session['mes_fin']
    
    if request.session['anio_fin']:
        params['anio_hasta'] = request.session['anio_fin']
        
    return Informe.objects.filter(** params)
    
        
        
        
        
        
        
        