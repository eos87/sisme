# -*- coding: UTF-8 -*-
from django.contrib import admin
from django.contrib.auth.models import Group
from models import *
from fed.models import *

class AccionImpulsadaInline(admin.TabularInline):
    verbose_name_plural = '1.1.1 Acciones impulsadas que posicionan el tema de equidad e igualdad'
    model = AccionImpulsada
    template = 'admin/contraparte/informe/tabular.html'
    extra = 1
    resultado = 'R1.1 Impulsando acciones para la aplicación de leyes, códigos, reglamentos, normativas y políticas públicas para la igualdad y equidad de género'
    
class AccionImplementadaInline(admin.TabularInline):
    verbose_name_plural = '1.1.1 Acciones implementadas que posicionan el tema de equidad e igualdad'
    model = AccionImplementada
    extra = 1
    
class ParticipacionComisionInline(admin.TabularInline):
    verbose_name_plural = '1.1.2 Participación en comisiones para incidir sobre toma de decisiones sobre DDSSRR y equidad'
    model = ParticipacionComision
    extra = 1
    
class AgendaPublicaInline(admin.TabularInline):
    verbose_name_plural = '1.1.3 Organizaciones que mantienen en la agenda pública la defensa de los DDSSRR, incluyendo el derecho al aborto terapéutico.'
    model = AgendaPublica
    extra = 1

class ObservatorioInline(admin.TabularInline):
    verbose_name_plural = '1.1.4 Observatorios para la vigilancia de la restitución, creación y aplicación de leyes, políticas, acciones y servicios en torno a los DDSSRR.'
    model = Observatorio
    extra = 1
    
PERMISOS = {
            1: [AccionImpulsadaInline, AccionImplementadaInline, ParticipacionComisionInline, AgendaPublicaInline, ObservatorioInline],
            2: []            
            }

#funcion para obtener los permisos del proyecto
def get_proy_perms(obj):    
    perms = []
    for code in obj.proyecto.resultados.all().values_list('codigo'):
        perms += PERMISOS[code[0]]                          
    
    return perms

class InformeAdmin(admin.ModelAdmin):
    list_display = ['organizacion', 'proyecto', 'desde', 'hasta']
    search_fields = ['organizacion__nombre', 'organizacion__nombre_corto', 'organizacion__codigo', 'proyecto__nombre', 'proyecto__codigo']
    #raw_id_fields = ('proyecto',)    
    add_form_template = 'admin/contraparte/informe/add_template.html'    
    fieldsets = [
        (None, {'fields': ['organizacion', 'proyecto']}),
        (u'Inicio de período', {'fields': [('anio_desde', 'mes_desde'),]}),
        (u'Fin de período', {'fields': [('anio_hasta', 'mes_hasta')]}),        
    ]
    inlines = []
    
    #sobreescribiendo el metodo para filtrar los objetos    
    def queryset(self, request):
        grupos = request.user.groups.all()
        fed = Group.objects.get(name='Equipo Fed')
        if request.user.is_superuser or fed in grupos:
            return Informe.objects.all()
        return Informe.objects.filter(organizacion__user=request.user)
    
    def get_form(self, request, obj=None, ** kwargs):
        #CODIGO ENCARGADO MOSTRAR INLINES SE MUESTRAN EN AL ADMIN
        self.inline_instances = []
        if not obj == None:
            for inline_class in get_proy_perms(obj):
                inline_instance = inline_class(self.model, self.admin_site)
                self.inline_instances.append(inline_instance)
        
        grupos = request.user.groups.all()
        fed = Group.objects.get(name='Equipo Fed')
        if request.user.is_superuser or fed in grupos:        
            form = super(InformeAdmin, self).get_form(request, ** kwargs)
        else:
            form = super(InformeAdmin, self).get_form(request, ** kwargs)
            form.base_fields['organizacion'].queryset = request.user.organizacion_set.all()
            form.base_fields['proyecto'].queryset = Proyecto.objects.filter(organizacion__in = request.user.organizacion_set.all())            
        return form
    
    def get_formsets(self, request, obj=None):
        self.inline_instances = []
        if not obj == None:       
            for inline_class in get_proy_perms(obj):
                inline_instance = inline_class(self.model, self.admin_site)
                self.inline_instances.append(inline_instance)
                
        for inline in self.inline_instances:
            yield inline.get_formset(request, obj)

admin.site.register(Informe, InformeAdmin)
admin.site.register(Comision)
admin.site.register(AccionAgenda)
admin.site.register(TipoObservatorio)



