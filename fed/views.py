# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from forms import GralForm

def generales(request):
    if request == 'POST':
        form = GralForm(request.POST)
    else:
        form = GralForm()
    return render_to_response("fed/generales.html", RequestContext(request, locals()))
