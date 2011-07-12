from django.shortcuts import render_to_response
from django.template.context import RequestContext
from fed.forms import GanttForm
from fed.models import Proyecto, Organizacion
import datetime

def index(request):
    estilos = {1: 'month_estilo_1', 2: 'month_estilo_2', 3: 'month_estilo_3',
               4: 'month_estilo_1', 5: 'month_estilo_2', 6: 'month_estilo_3'}
    proys = {}
    if request.method == 'POST':
        form = GanttForm(request.POST)
        if form.is_valid():
            organizacion = form.cleaned_data['organizacion']
            for proyecto in organizacion.proyecto_set.all():
                proys[proyecto.codigo] = {mes: have_informe(proyecto, mes, form.cleaned_data['anio']) for mes in range(1,13)}
    else:
        form = GanttForm()
        organizacion = Organizacion.objects.all().order_by('?')[0]
        for proyecto in organizacion.proyecto_set.all():
            proys[proyecto.codigo] = {mes: have_informe(proyecto, mes, datetime.date.today().year) for mes in range(1,13)}    
    
    return render_to_response('index.html', RequestContext(request, locals()))


def have_informe(proyecto, mes, year):
    try:
        inform = proyecto.informe_set.get(mes=mes, anio=year)
        return True
    except:
        return False