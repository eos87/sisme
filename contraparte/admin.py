# -*- coding: UTF-8 -*-
from django.contrib import admin
from django.contrib.auth.models import Group
from models import *
from sisme.fed.models import *
from django.contrib.admin.models import LogEntry

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['action_time', 'user', 'content_type', 'object_id', 'action_flag', 'change_message']
    list_filter = ['user']

admin.site.register(LogEntry, LogEntryAdmin)

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
    
#--------------------------- Resultado 1.2 ---------------------------------
class DemandaJusticiaInline(admin.TabularInline):
    verbose_name_plural = '1.2.1 OSC que impulsan acciones públicas demandado justicia, igualdad y la no discriminación en contra de las personas LGBTTTI, con discapacidad, etnia e indígena y PVVS'
    model = DemandaJusticia
    template = 'admin/contraparte/informe/tabular.html'
    extra = 1
    resultado = 'R1.2. Demandando justicia, la igualdad y no discriminación de las personas, independientemente de su sexo, orientación sexual, raza, etnia, condición física, o de las personas que viven con VIH y SIDA'
        
class DenunciaInline(admin.TabularInline):
    verbose_name_plural = '1.2.1 OSC  que impulsan denuncias demandado justicia, igualdad y la no discriminación ante instancias del Estado en contra de las personas'
    model = Denuncia
    extra = 1
    
#--------------------------- Resultado 2.1 ----------------------------------
class PoseenInfoInline(admin.StackedInline):
    verbose_name_plural = '2.1.1 Porcentaje de mujeres en las áreas de cobertura de las OCP que poseen información que les permite tomar decisiones sexuales y reproductivas de manera autónoma y bien informada'
    verbose_name = 'actividad'
    model = PoseenInfo
    template = 'admin/contraparte/informe/stacked.html'
    extra = 1
    resultado = 'R2.1. Involucramiento de las poblaciones metas en procesos de reflexión sobre los DDSSRR, dirigidos a una sexualidad integral, placentera, responsable, segura y libre de prejuicios.'
    mujeres_titles = [u'Niñas', u'Adol', u'Jóv', 'Adul']
    hombres_titles = [u'Niños', u'Adol', u'Jóv', 'Adul']
    lgbt_titles = [u'Trans', u'Lesb', u'Gay', 'HSH']
    fieldsets = [
        (None, {'fields': [('nombre', 'tipo_accion', 'tema'),]}),
        ('mujeres', {'fields': ['muj_ninas', 'muj_adols', 'muj_jovenes', 'muj_adultas',  
                                'muj_disca_ninas', 'muj_disca_adols', 'muj_disca_jovenes', 'muj_disca_adultas', 
                                'muj_etnia_ninas', 'muj_etnia_adols', 'muj_etnia_jovenes', 'muj_etnia_adultas',
                                'muj_vih_ninas', 'muj_vih_adols', 'muj_vih_jovenes', 'muj_vih_adultas']}),
        ('hombres', {'fields': ['hom_ninos', 'hom_adols', 'hom_jovenes', 'hom_adultos',  
                                'hom_disca_ninos', 'hom_disca_adols', 'hom_disca_jovenes', 'hom_disca_adultos', 
                                'hom_etnia_ninos', 'hom_etnia_adols', 'hom_etnia_jovenes', 'hom_etnia_adultos',
                                'hom_vih_ninos', 'hom_vih_adols', 'hom_vih_jovenes', 'hom_vih_adultos']}),
        ('lgbt', {'fields': ['lgbt_trans', 'lgbt_lesbi', 'lgbt_gay', 'lgbt_hsh']})                                             
    ]

class RecibenInfoInline(admin.TabularInline):
    verbose_name_plural = '2.1.4 Porcentaje de personas en las áreas de cobertura de las OCP que reciben información sobre VIH y SIDA, incluyendo las que viven con VIH.'
    model = RecibenInfo
    template = 'admin/contraparte/informe/stacked.html'
    extra = 1
    mujeres_titles = [u'Niñas', u'Adol', u'Jóv', 'Adul']
    hombres_titles = [u'Niños', u'Adol', u'Jóv', 'Adul']
    lgbt_titles = [u'Trans', u'Lesb', u'Gay', 'HSH']
    fieldsets = [
        (None, {'fields': [('nombre', 'tipo_accion'),]}),
        ('mujeres', {'fields': ['muj_ninas', 'muj_adols', 'muj_jovenes', 'muj_adultas',  
                                'muj_disca_ninas', 'muj_disca_adols', 'muj_disca_jovenes', 'muj_disca_adultas', 
                                'muj_etnia_ninas', 'muj_etnia_adols', 'muj_etnia_jovenes', 'muj_etnia_adultas',
                                'muj_vih_ninas', 'muj_vih_adols', 'muj_vih_jovenes', 'muj_vih_adultas']}),
        ('hombres', {'fields': ['hom_ninos', 'hom_adols', 'hom_jovenes', 'hom_adultos',  
                                'hom_disca_ninos', 'hom_disca_adols', 'hom_disca_jovenes', 'hom_disca_adultos', 
                                'hom_etnia_ninos', 'hom_etnia_adols', 'hom_etnia_jovenes', 'hom_etnia_adultos',
                                'hom_vih_ninos', 'hom_vih_adols', 'hom_vih_jovenes', 'hom_vih_adultos']}),
        ('lgbt', {'fields': ['lgbt_trans', 'lgbt_lesbi', 'lgbt_gay', 'lgbt_hsh']})                                             
    ]

#--------------------------- Resultado 2.2 ----------------------------------    
class PrevencionVBGInline(admin.TabularInline):
    verbose_name_plural = '2.2.1 Número y tipo de acciones emprendidas por las organizaciones contrapartes del FED que actúan individual o articuladas en la prevención de la VBG.'
    model = PrevencionVBG
    template = 'admin/contraparte/informe/stacked.html'
    extra = 1
    resultado = 'R2.2 Fortalecida la prevención de la violencia basada en género.'
    mujeres_titles = [u'Niñas', u'Adol', u'Jóv', 'Adul']
    hombres_titles = [u'Niños', u'Adol', u'Jóv', 'Adul']
    lgbt_titles = [u'Trans', u'Lesb', u'Gay', 'HSH']
    fieldsets = [
        (None, {'fields': [('nombre', 'tipo_accion'),]}),
        ('mujeres', {'fields': ['muj_ninas', 'muj_adols', 'muj_jovenes', 'muj_adultas',  
                                'muj_disca_ninas', 'muj_disca_adols', 'muj_disca_jovenes', 'muj_disca_adultas', 
                                'muj_etnia_ninas', 'muj_etnia_adols', 'muj_etnia_jovenes', 'muj_etnia_adultas',
                                'muj_vih_ninas', 'muj_vih_adols', 'muj_vih_jovenes', 'muj_vih_adultas']}),
        ('hombres', {'fields': ['hom_ninos', 'hom_adols', 'hom_jovenes', 'hom_adultos',  
                                'hom_disca_ninos', 'hom_disca_adols', 'hom_disca_jovenes', 'hom_disca_adultos', 
                                'hom_etnia_ninos', 'hom_etnia_adols', 'hom_etnia_jovenes', 'hom_etnia_adultos',
                                'hom_vih_ninos', 'hom_vih_adols', 'hom_vih_jovenes', 'hom_vih_adultos']}),
        ('lgbt', {'fields': ['lgbt_trans', 'lgbt_lesbi', 'lgbt_gay', 'lgbt_hsh']})                                             
    ]

class MasculinidadLibreInline(admin.TabularInline):
    verbose_name_plural = '2.2.3 Número y tipo de acciones especificas que promueven la masculinidad libre de prejuicios y violencia'
    model = MasculinidadLibre
    template = 'admin/contraparte/informe/stacked.html'
    extra = 1
    mujeres_titles = [u'Niñas', u'Adol', u'Jóv', 'Adul']
    hombres_titles = [u'Niños', u'Adol', u'Jóv', 'Adul']
    lgbt_titles = [u'Trans', u'Lesb', u'Gay', 'HSH']
    fieldsets = [
        (None, {'fields': [('nombre', 'tipo_accion'),]}),
        ('mujeres', {'fields': ['muj_ninas', 'muj_adols', 'muj_jovenes', 'muj_adultas',  
                                'muj_disca_ninas', 'muj_disca_adols', 'muj_disca_jovenes', 'muj_disca_adultas', 
                                'muj_etnia_ninas', 'muj_etnia_adols', 'muj_etnia_jovenes', 'muj_etnia_adultas',
                                'muj_vih_ninas', 'muj_vih_adols', 'muj_vih_jovenes', 'muj_vih_adultas']}),
        ('hombres', {'fields': ['hom_ninos', 'hom_adols', 'hom_jovenes', 'hom_adultos',  
                                'hom_disca_ninos', 'hom_disca_adols', 'hom_disca_jovenes', 'hom_disca_adultos', 
                                'hom_etnia_ninos', 'hom_etnia_adols', 'hom_etnia_jovenes', 'hom_etnia_adultos',
                                'hom_vih_ninos', 'hom_vih_adols', 'hom_vih_jovenes', 'hom_vih_adultos']}),
        ('lgbt', {'fields': ['lgbt_trans', 'lgbt_lesbi', 'lgbt_gay', 'lgbt_hsh']})                                             
    ]
    
#------------------------- Resultado 2.3 -------------------------------------
class CasoAtendidoInline(admin.TabularInline):
    verbose_name_plural = '2.3.1 Número de casos atendidos por las organizaciones contrapartes del FED a través de los servicios de atención en salud, psicológica y legal para víctimas de violencia.'
    model = CasoAtendido
    template = 'admin/contraparte/informe/tabular.html'
    extra = 1
    resultado = 'R2.3 Acceso a servicios de atención integral y demanda de salud y justicia para las victimas de violencia de género.'

class DenunciaInterpuestaInline(admin.TabularInline):
    verbose_name_plural = '2.3.2 Número de denuncias interpuestas por las víctimas de violencia en las instancias que administran justicia como producto de las acciones de las organizaciones de la sociedad civil apoyadas por el FED.'
    model = DenunciaInterpuesta
    extra = 1
    
class AtencionMujerInline(admin.TabularInline):
    verbose_name_plural = '2.3.4. Número de mujeres atendidas en los albergues apoyados por  el FED como instrumento para la construcción de nuevos proyectos de vida.'
    model = AtencionMujer
    extra = 1
    template = 'admin/contraparte/informe/tabular.html'
    resultado = 'R2.3 (Atención en albergues) Acceso a servicios de atención integral y demanda de salud y justicia para las victimas de violencia de género'

class ReferenciaContraReferenciaInline(admin.TabularInline):
    verbose_name_plural = '2.3.5. Número de referencia y contra referencias que realizan las OCP del FED con instituciones públicas.'
    model = ReferenciaContraReferencia
    extra = 1

#------------------------- Resultado 3.1 -------------------------------------
class CapacidadAdmitivaInline(admin.TabularInline):
    verbose_name_plural = '3.1.3. Porcentaje y número de OCP que mejoran sus capacidades administrativas y de gestión.'
    model = CapacidadAdmitiva
    template = 'admin/contraparte/informe/tabular.html'
    extra = 1
    resultado = 'R.3.1 Fortalecida la capacidad técnica de las OSC contrapartes del FED.'
    
class MedirReportarInline(admin.TabularInline):
    verbose_name_plural = '3.1.3 Han mejorado las capacidades para medir y reportar los indicadores propuestos con apoyo del FED '
    model = MedirReportar
    extra = 1

class PlanEstrategicoInline(admin.TabularInline):
    verbose_name_plural = '3.1.3 Utilizan su plan estratégico para mejorar sus capacidades'
    model = PlanEstrategico
    extra = 1

PERMISOS = {
            1: [AccionImpulsadaInline, AccionImplementadaInline, ParticipacionComisionInline, AgendaPublicaInline],
            2: [DemandaJusticiaInline, DenunciaInline],
            3: [PoseenInfoInline, RecibenInfoInline],
            4: [PrevencionVBGInline, MasculinidadLibreInline], 
            5: [CasoAtendidoInline, DenunciaInterpuestaInline, ReferenciaContraReferenciaInline],
            6: [CapacidadAdmitivaInline, MedirReportarInline, PlanEstrategicoInline],
            7: [AtencionMujerInline, ]           
            }

#funcion para obtener los permisos del proyecto
def get_proy_perms(obj):    
    perms = []
    for code in obj.proyecto.resultados.all().values_list('codigo'):
        perms += PERMISOS[code[0]]                          
    
    return perms

class InformeAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_top = True
    list_display = ['organizacion', 'proyecto', 'mes', 'anio']
    list_filter = ['organizacion', 'proyecto']
    search_fields = ['organizacion__nombre', 'organizacion__nombre_corto', 'organizacion__codigo', 'proyecto__nombre', 'proyecto__codigo']    
    add_form_template = 'admin/contraparte/informe/add_template.html'    
    fieldsets = [
        (None, {'fields': ['organizacion', 'proyecto']}),
        (u'Período de reporte', {'fields': [('anio', 'mes'),]}),                
    ]
    inlines = []
    
    class Media:
        js = ('/files/js/validar_fecha.js',)
              
    
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
admin.site.register(TipoObservatorio)



