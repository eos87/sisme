# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
from sisme.fed.models import Proyecto
from sisme.contraparte.models import Informe
from django.utils import simplejson

def save_as_xls(request):
    tabla = request.POST['tabla']    
    response = render_to_response('xls.html', {'tabla': tabla, })
    response['Content-Disposition'] = 'attachment; filename=tabla.xls'
    response['Content-Type'] = 'application/vnd.ms-excel'
    response['Charset'] ='UTF-8'
    return response

def get_orgs(request):
    ids = request.GET.get('ids', '')
    mod_ids = [int(id) for id in ids.split(',') if ids]
    orgs = [{'nombre_corto': x.organizacion.nombre_corto,'id':x.organizacion.id} for x in Proyecto.objects.filter(modalidad__in=mod_ids)]    
    
    return HttpResponse(simplejson.dumps(orgs), mimetype='application/json')

def ajax_meses(request):    
    from sisme.contraparte.models import MESES     
    
    proy_id = request.GET.get('id', '')
    anio = request.GET.get('year', '')
    load = request.GET.get('load', '')
    if proy_id and anio:
        dicc_mes = []        
        meses = list(Informe.objects.filter(proyecto__id=int(proy_id), anio=int(anio)).values_list('mes', flat=True))
        if load:
            meses.remove(int(load))
        for mes in [id for id in range(1,13)]:
            if mes not in meses:
                dicc_mes.append({'id': mes, 'nombre': MESES[mes-1][1]})
            
    return HttpResponse(simplejson.dumps(dicc_mes), mimetype='application/json')        
        
def view_graph(request):
    var = request.POST['data']
    return HttpResponse(var, mimetype='text/plain')
    
    
    
    
    
    
    
    
    
    
    