# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from forms import GralForm
from models import *
from sisme.lugar.models import *

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
    
    #orgs_filtradas = len([proy.organizacion for proy in proyectos_filtrados])
    
       
    #organizaciones por modalidad de apoyo
    tabla_modalidad = {}  
    total_orgs = 0
    
    for op in MODALIDAD_CHOICE:
        orgs_2010 = Organizacion.objects.filter(proyecto__in=proyectos_filtrados, 
                                                proyecto__modalidad=op[0], 
                                                proyecto__fecha_inicio__year=2010).values_list('nombre_corto', flat=True)
        orgs_2011 = Organizacion.objects.filter(proyecto__in=proyectos_filtrados, 
                                                proyecto__modalidad=op[0], 
                                                proyecto__fecha_inicio__year=2011).values_list('nombre_corto', flat=True)
        lista1 = list(set(orgs_2010))
        lista2 = list(set(orgs_2011))
        total_orgs += len(lista1)
        total_orgs += len(lista2)
        tabla_modalidad[op[1]] = {'cantidad1': len(lista1), '2010': lista1,
                                  'cantidad2': len(lista2), '2011': lista2,}
        
    #organizaciones por modalidad que han finalizado
    tabla_modalidad_finalizado = {}
    fecha_actual = datetime.date.today()
    total_orgs_fin = 0
    
    for op in MODALIDAD_CHOICE:
        #orgs = ['%s-<b>%s</b>' % (proyecto.organizacion.nombre_corto, proyecto.codigo) for proyecto in proyectos_filtrados.filter(modalidad=op[0],fecha_fin__lte=fecha_actual)] 
        orgs = Organizacion.objects.filter(proyecto__in=proyectos_filtrados,
                                           proyecto__modalidad=op[0],
                                           proyecto__fecha_fin__lte=fecha_actual).values_list('nombre_corto', flat=True)
                                                                                                                                 
        total_orgs_fin += len(orgs)
        tabla_modalidad_finalizado[op[1]] = {'cantidad': len(orgs), 'organizaciones': orgs}
        
    #cobertura de los proyectos
    tabla_cobertura = {}
    for op in COBERTURA:
        proys = proyectos_filtrados.filter(cobertura=op[0])
        tabla_cobertura[op[1]] = proys
        
    #organizacion y montos de proyectos
    tabla_montos = {}        
    for proy in proyectos_filtrados:
        org_name = proy.organizacion
        if org_name in tabla_montos:
            tabla_montos[org_name].append(proy)
        else:
            tabla_montos[org_name] = [proy,]  
    
    #tablas por poblacion meta
    tabla_poblacion_meta = {}
    for op in MODALIDAD_CHOICE:
        if not op in tabla_poblacion_meta:
            tabla_poblacion_meta[op] = {}
            
        for proy in proyectos_filtrados.filter(modalidad=op[0]):
            org = proy.organizacion            
            if org in tabla_poblacion_meta[op]:
                tabla_poblacion_meta[op][org].append(proy)
            else:
                tabla_poblacion_meta[op][org] = [proy, ]
            
    #resultados a los que aportan los proyectos
    tabla_resultados = {}
    resultados = Resultado.objects.all()
    for proyecto in proyectos_filtrados:
        if not proyecto in tabla_resultados: 
            tabla_resultados[proyecto] = {}            
        for resultado in resultados:
            if resultado in proyecto.resultados.all():
                tabla_resultados[proyecto][resultado.codigo] = 1
            else:
                tabla_resultados[proyecto][resultado.codigo] = 0
                
    #cobertura de las organizaciones por municipios
    tabla_cobertura_municipios = {}
    for org in [proy.organizacion for proy in proyectos_filtrados]:
        tabla_cobertura_municipios[org] = {}
        lista = []
        for proyecto in proyectos_filtrados.filter(organizacion=org):
            for depa in Departamento.objects.filter(municipio__tematrabajo__proyecto=proyecto):
                tabla_cobertura_municipios[org][depa.nombre] = Municipio.objects.filter(tematrabajo__proyecto=proyecto, 
                                                                                        departamento=depa).distinct().values_list('nombre', 
                                                                                                                       flat=True)
                
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












