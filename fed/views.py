# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from forms import GralForm
from models import *

def generales(request):    
    if request.method == 'POST':
        form = GralForm(request.POST)
        if form.is_valid():
            request.session['gral_year'] = form.cleaned_data['year']
    else:
        form = GralForm()
        request.session['gral_year'] = 0
    
    params = {}
    if request.session['gral_year'] != 0:
        params['fecha_inicio__year'] = request.session['gral_year']
    
    #organizaciones por modalidad de apoyo
    tabla_modalidad = {}
    for op in MODALIDAD_CHOICE:
        orgs = [proyecto.organizacion.nombre_corto for proyecto in Proyecto.objects.filter(modalidad=op[0], ** params)]
        lista = list(set(orgs))
        tabla_modalidad[op[1]] = {'cantidad': len(lista), 'organizaciones': lista}
    
    return render_to_response("fed/generales.html", RequestContext(request, locals()))
