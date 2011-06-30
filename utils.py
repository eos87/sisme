# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
from sisme.fed.models import Proyecto
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