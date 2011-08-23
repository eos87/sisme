# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from forms import GralForm
from models import *

def generales(request):    
    if request.method == 'POST':
        form = GralForm(request.POST)
        if form.is_valid():
            request.session['gral_year'] = int(form.cleaned_data['year'])
    else:
        form = GralForm()
        request.session['gral_year'] = 0
    
    if request.session['gral_year'] != 0:        
        proyectos_filtrados = Proyecto.objects.filter(fecha_inicio__year=request.session['gral_year'])
    else:
        proyectos_filtrados = Proyecto.objects.all()
    
    
    orgs_filtradas = len(list(set([proy.organizacion for proy in proyectos_filtrados])))
    
    #organizaciones por modalidad de apoyo
    tabla_modalidad = {}
    for op in MODALIDAD_CHOICE:
        orgs = [proyecto.organizacion.nombre_corto for proyecto in proyectos_filtrados.filter(modalidad=op[0])]
        lista = list(set(orgs))
        tabla_modalidad[op[1]] = {'cantidad': len(lista), 'organizaciones': lista}
        
    #cobertura de los proyectos
    tabla_cobertura = {}
    for op in COBERTURA:
        proys = proyectos_filtrados.filter(cobertura=op[0])
        tabla_cobertura[op[1]] = proys
        
    #organizacion y montos de proyectos
    tabla_montos = {}
    orgs = [proyecto.organizacion for proyecto in proyectos_filtrados]
    for org in orgs:
        tabla_montos[org] = proyectos_filtrados.filter(organizacion=org)
    
    #tablas por poblacion meta
    tabla_poblacion_meta = {}
    for op in MODALIDAD_CHOICE:
        organizaciones_meta = [proyecto.organizacion for proyecto in proyectos_filtrados.filter(modalidad=op[0])]
        for org in organizaciones_meta:
            tabla_poblacion_meta[op] = {}
        for org in organizaciones_meta:
            tabla_poblacion_meta[op][org] = proyectos_filtrados.filter(organizacion=org)  
            
    #resultados a los que aportan los proyectos
    tabla_resultados = {}
    resultados = Resultado.objects.all()
    for proyecto in proyectos_filtrados:
        for resultado in resultados:
            for resultado in resultados:
                tabla_resultados[proyecto] = {}            
            for resultado in resultados:
                if resultado in proyecto.resultados.all():
                    tabla_resultados[proyecto][resultado.codigo] = 1
                else:
                    tabla_resultados[proyecto][resultado.codigo] = 0
                    
    #cobertura de las organizaciones por municipios
    tabla_cobertura_municipios = {}
    for org in [proy.organizacion for proy in proyectos_filtrados]:
        lista = []
        for proyecto in proyectos_filtrados.filter(organizacion=org):
            for tema in proyecto.tematrabajo_set.all():
                for municipio in tema.municipio.all():
                    lista.append(municipio)
        tabla_cobertura_municipios[org] = list(set(lista))
        
    #cobertura por temas
    temas = Tema.objects.all()
    tabla_temas = {}
    for tema in temas:
        lista = []        
        for tematrabajo in TemaTrabajo.objects.filter(tema=tema, proyecto__in=proyectos_filtrados):
            for municipio in tematrabajo.municipio.all():
                lista.append(municipio)
        tabla_temas[tema] = list(set(lista))              
    
    return render_to_response("fed/generales.html", RequestContext(request, locals()))












