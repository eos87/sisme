from django.shortcuts import render_to_response
from django.template.context import RequestContext
from forms import InfluenciaForm

def indicadores(request):
    form = InfluenciaForm()
    return render_to_response('contraparte/indicadores.html', RequestContext(request, locals()))
