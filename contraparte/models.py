# -*- coding: UTF-8 -*-
from django.db import models
from sisme.fed.models import *

YEARS = ((2011, '2011'),)
MESES = ((1, 'Enero'), (2, 'Febrero'),
         (3, 'Marzo'), (4, 'Abril'),
         (5, 'Mayo'), (6, 'Junio'),
         (7, 'Julio'), (8, 'Agosto'),
         (9, 'Septiembre'), (10, 'Octube'),
         (11, 'Noviembre'), (12, 'Diciembre'))

ACCIONES = ((1, 'Reuniones/encuentros con autoridades'),
            (2, 'Foros con autoridades'),
            (3, u'Participación en cabildos'),
            (4, 'Cabildeos con tomadores de decisiones'))

class Informe(models.Model):
    organizacion = models.ForeignKey(Organizacion)
    proyecto = models.ForeignKey(Proyecto)
    mes = models.IntegerField(choices=MESES, verbose_name=u'Mes')
    anio = models.IntegerField(choices=YEARS, verbose_name=u'Año')        
    
    def __unicode__(self):
        return u'%s | Período: %s-%s' % (self.organizacion.nombre_corto, self.get_mes_display(), self.anio)
    
    class Meta:
        verbose_name_plural = u'Informes'        

AMBITO = ((1, 'Municipales'), (2, 'Departamentales'), (3, 'Nacional'), (4, u'Regiones Autónomas'))
    
class AccionImpulsada(models.Model):
    informe = models.ForeignKey(Informe)
    nombre = models.CharField(max_length=200, verbose_name='Nombre de la actividad')
    tipo_accion = models.IntegerField(choices=ACCIONES)
    tema = models.ForeignKey(Tema)
    hombres = models.IntegerField('No. de participantes hombres')
    mujeres = models.IntegerField('No. de participantes mujeres')
    ambito = models.IntegerField(choices=AMBITO, verbose_name=u'Ámbito territorial')
    
    def __unicode__(self):
        return u'%s - %s' % (self.informe, self.id)
    
    class Meta:
        verbose_name_plural = 'Acciones Impulsadas'
        
ACCION = ((1, 'Leyes'), (2, 'Decretos'), (3, 'Reglamentos'),
          (4, 'Ordenanzas Municipales'), (5, 'Normativas'), (6, 'Acuerdos'))

ESTADO_ACCION = ((1, 'Introducida'), (2, 'En proceso'), (3, 'Aprobada'))

class AccionImplementada(models.Model):
    informe = models.ForeignKey(Informe)
    nombre = models.CharField(max_length=200, verbose_name='Nombre de la actividad')
    accion = models.IntegerField(choices=ACCION)
    tema = models.ForeignKey(Tema)
    estado = models.IntegerField(choices=ESTADO_ACCION)
    
    def __unicode__(self):
        return u'%s - %s' % (self.informe, self.id)
    
    class Meta:
        verbose_name_plural = 'Acciones Implementadas'

COMISION_CHOICE = ((1, u'Comisión de la Niñez y Adolescencia'),
                   (2, u'Comisión de género / mujer'),
                   (3, u'Comisión de Salud'),
                   (4, u'Comisión de lucha contra el SIDA'),
                   (5, u'Comisión de seguimiento a la aplicación del código penal'),
                   (6, u'Comisión de prevención de la violencia'))
    
class ParticipacionComision(models.Model):
    informe = models.ForeignKey(Informe)
    nombre = models.CharField(max_length=200, verbose_name='Nombre de la actividad')    
    comision = models.IntegerField(choices=COMISION_CHOICE)
    ambito = models.IntegerField(choices=AMBITO, verbose_name=u'Ámbito territorial')
    estado = models.IntegerField(choices=ESTADO_ACCION, verbose_name=u'Efectividad de la acción')    
    
    def __unicode__(self):
        return u'%s - %s' % (self.informe, self.id)
    
    verbose_name = u'Participación en Comisiones'
    verbose_name_plural = u'Participaciones en Comisiones'
    
ACCIONES2 = ((1, u'Campañas de televisión'), (2, u'Campañas radiales'), (3, u'Artítulos de periódicos'))

class AgendaPublica(models.Model):
    informe = models.ForeignKey(Informe)
    nombre = models.CharField(max_length=200, verbose_name='Nombre de la actividad')
    tipo_accion = models.IntegerField(choices=ACCIONES2)
    tema = models.ForeignKey(Tema)    
    ambito = models.IntegerField(choices=AMBITO, verbose_name=u'Ámbito territorial')
    
    def __unicode__(self):
        return u'%s - %s' % (self.informe, self.id)
    
    verbose_name = u'Agenda Pública'
    verbose_name_plural = u'Agenda Pública'
    
class TipoObservatorio(models.Model):
    nombre = models.CharField(max_length=150)
    
    def __unicode__(self):
        return '%s' % self.nombre
    
    class Meta:
        verbose_name = u'Tipo de Observatorio'
        verbose_name_plural = 'Tipos de Observatorios'

ACCION_OBSERVATORIO = ((1, u'Divulgaciones de investigación'),
                       (2, u'Divulgación de estudios'),
                       (3, u'Divulgación de agendas de actividades de interés para las organizaciones'),
                       (4, u'Divulgación de actividades públicas periódicas'),
                       (5, u'Divulgación de Boletín electrónico'),
                       (6, u'Comunicación hacia los medios'),
                       (7, u'Mantención y actualización del portal Web del Observatorio'),
                       (8, u'Elaboración de informes'),
                       (9, u'Columnas de opinión'),
                       (10, u'Análisis y el debate con artículos, entrevistas, opiniones y estadísticas'),
                       (11, u'Foro de discusión'),
                       (12, u'Seminarios'))    

class Observatorio(models.Model):
    informe = models.ForeignKey(Informe)
    tipo_observatorio = models.ForeignKey(TipoObservatorio)
    accion = models.IntegerField(choices=ACCION_OBSERVATORIO)
    
    def __unicode__(self):
        return u'%s - %s' % (self.informe, self.id)
    
    class Meta:    
        verbose_name = u'Observatorio'
        verbose_name_plural = u'Observatorios'        
    
#------------------------------ Resultado 1.2 --------------------------------------
POBLACION = ((1, u'En contra de las discriminación a personas LGBT'), 
             (2, u'En contra de la discriminación a personas discapacitadas'), 
             (3, u'En contra de la discriminación a personas con VIH'), 
             (4, u'En contra de la discriminación por etnias'),
     	     (5, u'En contra de la discriminación a la mujer'))

ACCION_DEMANDA = ((1, u'Campañas en televisión '),
                  (2, u'Marchas/plantones'),
                  (3, u'Campañas en radio'),
                  (4, u'Foros'))

class DemandaJusticia(models.Model):
    informe = models.ForeignKey(Informe)
    nombre = models.CharField(max_length=200, verbose_name='Nombre de la actividad')    
    accion = models.IntegerField(choices=ACCION_DEMANDA)
    poblacion_discriminada = models.IntegerField(choices=POBLACION)
    
    def __unicode__(self):
        return u'%s - %s' % (self.informe, self.id)
    
    class Meta:
        verbose_name = u'Demanda de Justicia'
        verbose_name_plural = u'Demandas de Justicia'
    
DENUNCIAS = ((1, u'Denuncias realizadas'), (2, u'Atendidas por las instancias correspondientes'), (3, u'Denuncias divulgadas'))
TIPO_POBLACION = ((1, u'LGBT'), (2, u'Discapacitados/as'), (3, u'VIH'), (4, u'Étnica e indígena'))

class Denuncia(models.Model):
    informe = models.ForeignKey(Informe)
    nombre = models.CharField(max_length=200, verbose_name='Nombre de la actividad')
    situacion = models.IntegerField(choices=DENUNCIAS)
    tipo_poblacion = models.IntegerField(choices=TIPO_POBLACION)    
    
    def __unicode__(self):
        return u'%s - %s' % (self.informe, self.id)
    
    class Meta:
        verbose_name = u'Denuncia'
        verbose_name_plural = u'Denuncias'  
    
#------------------------------- Resultado 2.1 ---------------------------------
ACCION_POSEE_INFO = ((1, u'Talleres de formación'), 
                     (2, u'Círculos de estudio'), 
                     (3, u'Videos reflexivos'), 
                     (4, u'Intercambios de experiencias'),
                     (5, u'Visitas de campo'),
                     (6, u'Consejería'))

TIPO_POBLACION2 = ((1, 'Mujeres'), 
                  (2, 'Hombres'), 
                  (3, u'LGBT'), 
                  (4, u'Discapacitados/as'), 
                  (5, u'VIH'), 
                  (6, u'Étnica e indígena'))

SEGMENTO_POBLACIONAL = ((1, u'Niñas'),
                        (2, u'Niños'),
                        (3, u'Adolescente'),
                        (4, u'Joven'),
                        (5, u'Adulta'),
                        (6, u'Adulto'),
                        (7, u'Trans'),
                        (8, u'Lesbiana'),
                        (9, u'Gay'),
                        (10, u'HSH'))

class PoseenInfo(models.Model):
    informe = models.ForeignKey(Informe)
    nombre = models.CharField(max_length=200, verbose_name='Nombre de la actividad')
    tipo_accion = models.IntegerField(choices=ACCION_POSEE_INFO)
    tema = models.ForeignKey(Tema)
    
    #------------ participantes mujeres ---------------
    muj_ninas = models.IntegerField(verbose_name=u'Niñas', default=0)
    muj_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    muj_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    muj_adultas = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ participantes mujeres discapacitadas ---------------
    muj_disca_ninas = models.IntegerField(verbose_name=u'Niñas', default=0)
    muj_disca_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    muj_disca_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    muj_disca_adultas = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ participantes mujeres etnicas ---------------
    muj_etnia_ninas = models.IntegerField(verbose_name=u'Niñas', default=0)
    muj_etnia_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    muj_etnia_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    muj_etnia_adultas = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ participantes mujeres vih ---------------
    muj_vih_ninas = models.IntegerField(verbose_name=u'Niñas', default=0)
    muj_vih_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    muj_vih_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    muj_vih_adultas = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ participantes HOMBRES ---------------
    hom_ninos = models.IntegerField(verbose_name=u'Niñas', default=0)
    hom_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    hom_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    hom_adultos = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ participantes HOMBRES discapacitados ---------------
    hom_disca_ninos = models.IntegerField(verbose_name=u'Niñas', default=0)
    hom_disca_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    hom_disca_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    hom_disca_adultos = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ participantes hombres etnicos ---------------
    hom_etnia_ninos = models.IntegerField(verbose_name=u'Niñas', default=0)
    hom_etnia_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    hom_etnia_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    hom_etnia_adultos = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ participantes hombres vih ---------------
    hom_vih_ninos = models.IntegerField(verbose_name=u'Niñas', default=0)
    hom_vih_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    hom_vih_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    hom_vih_adultos = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ LGBT participantes -------------------------
    lgbt_trans = models.IntegerField(verbose_name=u'Trans', default=0)
    lgbt_lesbi = models.IntegerField(verbose_name=u'Lesbianas', default=0)
    lgbt_gay = models.IntegerField(verbose_name=u'Gay', default=0)
    lgbt_hsh = models.IntegerField(verbose_name=u'HSH', default=0)    
    
    def __unicode__(self):
        return u'%s - %s' % (self.informe, self.id)
    
    class Meta:
        verbose_name = u'Posee información'
        verbose_name_plural = u'Poseen Información'
    
class RecibenInfo(models.Model):
    informe = models.ForeignKey(Informe)
    nombre = models.CharField(max_length=200, verbose_name='Nombre de la actividad')
    tipo_accion = models.IntegerField(choices=ACCION_POSEE_INFO)
        
    #------------ participantes mujeres ---------------
    muj_ninas = models.IntegerField(verbose_name=u'Niñas', default=0)
    muj_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    muj_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    muj_adultas = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ participantes mujeres discapacitadas ---------------
    muj_disca_ninas = models.IntegerField(verbose_name=u'Niñas', default=0)
    muj_disca_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    muj_disca_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    muj_disca_adultas = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ participantes mujeres etnicas ---------------
    muj_etnia_ninas = models.IntegerField(verbose_name=u'Niñas', default=0)
    muj_etnia_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    muj_etnia_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    muj_etnia_adultas = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ participantes mujeres etnicas ---------------
    muj_vih_ninas = models.IntegerField(verbose_name=u'Niñas', default=0)
    muj_vih_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    muj_vih_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    muj_vih_adultas = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ participantes HOMBRES ---------------
    hom_ninos = models.IntegerField(verbose_name=u'Niñas', default=0)
    hom_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    hom_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    hom_adultos = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ participantes HOMBRES discapacitados ---------------
    hom_disca_ninos = models.IntegerField(verbose_name=u'Niñas', default=0)
    hom_disca_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    hom_disca_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    hom_disca_adultos = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ participantes hombres etnicos ---------------
    hom_etnia_ninos = models.IntegerField(verbose_name=u'Niñas', default=0)
    hom_etnia_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    hom_etnia_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    hom_etnia_adultos = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ participantes hombres etnicas ---------------
    hom_vih_ninos = models.IntegerField(verbose_name=u'Niñas', default=0)
    hom_vih_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    hom_vih_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    hom_vih_adultos = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ LGBT participantes -------------------------
    lgbt_trans = models.IntegerField(verbose_name=u'Trans', default=0)
    lgbt_lesbi = models.IntegerField(verbose_name=u'Lesbianas', default=0)
    lgbt_gay = models.IntegerField(verbose_name=u'Gay', default=0)
    lgbt_hsh = models.IntegerField(verbose_name=u'HSH', default=0)  
    
    def __unicode__(self):
        return u'%s - %s' % (self.informe, self.id)
    
    class Meta:
        verbose_name = u'Recibe información'
        verbose_name_plural = u'Reciben Información' 

#------------------------------- Resultado 2.2 ---------------------------------
ACCION_PREVENCION = ((1, u'Campañas en Televisión'),
                     (2, u'Campañas radiales'),
                     (3, u'Artículos de periódicos'),
                     (4, u'Talleres'),
                     (5, u'Foros'),
                     (6, u'Intercambios de experiencias'),
                     (7, u'Visitas grupales o individuales'),
                     (8, u'Materiales educativos'),
                     (9, u'Reuniones con autoridades'),
                     (10, u'Consejeria y promotoria social'))
    
class BaseR22(models.Model):
    informe = models.ForeignKey(Informe)
    nombre = models.CharField(max_length=200, verbose_name='Nombre de la actividad')
    tipo_accion = models.IntegerField(choices=ACCION_PREVENCION)    
        
    #------------ participantes mujeres ---------------
    muj_ninas = models.IntegerField(verbose_name=u'Niñas', default=0)
    muj_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    muj_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    muj_adultas = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ participantes mujeres discapacitadas ---------------
    muj_disca_ninas = models.IntegerField(verbose_name=u'Niñas', default=0)
    muj_disca_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    muj_disca_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    muj_disca_adultas = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ participantes mujeres etnicas ---------------
    muj_etnia_ninas = models.IntegerField(verbose_name=u'Niñas', default=0)
    muj_etnia_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    muj_etnia_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    muj_etnia_adultas = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ participantes mujeres etnicas ---------------
    muj_vih_ninas = models.IntegerField(verbose_name=u'Niñas', default=0)
    muj_vih_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    muj_vih_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    muj_vih_adultas = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ participantes HOMBRES ---------------
    hom_ninos = models.IntegerField(verbose_name=u'Niñas', default=0)
    hom_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    hom_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    hom_adultos = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ participantes HOMBRES discapacitados ---------------
    hom_disca_ninos = models.IntegerField(verbose_name=u'Niñas', default=0)
    hom_disca_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    hom_disca_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    hom_disca_adultos = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ participantes hombres etnicos ---------------
    hom_etnia_ninos = models.IntegerField(verbose_name=u'Niñas', default=0)
    hom_etnia_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    hom_etnia_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    hom_etnia_adultos = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ participantes hombres etnicas ---------------
    hom_vih_ninos = models.IntegerField(verbose_name=u'Niñas', default=0)
    hom_vih_adols = models.IntegerField(verbose_name=u'Adolescentes', default=0)
    hom_vih_jovenes = models.IntegerField(verbose_name=u'Jóvenes', default=0)
    hom_vih_adultos = models.IntegerField(verbose_name=u'Adultas', default=0)
    
    #------------ LGBT participantes -------------------------
    lgbt_trans = models.IntegerField(verbose_name=u'Trans', default=0)
    lgbt_lesbi = models.IntegerField(verbose_name=u'Lesbianas', default=0)
    lgbt_gay = models.IntegerField(verbose_name=u'Gay', default=0)
    lgbt_hsh = models.IntegerField(verbose_name=u'HSH', default=0) 
    
    def __unicode__(self):
        return u'%s - %s' % (self.informe, self.id)
    
    class Meta:
        abstract = True

class PrevencionVBG(BaseR22):    
    
    class Meta:
        verbose_name = u'Prevención de VBG'
        verbose_name_plural = u'Prevención de VBG'
    
class MasculinidadLibre(BaseR22):
        
    class Meta:
        verbose_name = u'Masculinidad Libre'
        verbose_name_plural = u'Masculinidad Libre'
 
#-------------------------- Resultado 2.3 ----------------------------
TIPOS_CASOS = ((1, u'Médica'), (2, u'Psicológica'), (3, u'Legal'), (4, u'Atención General'))
SITUACION_CASOS = ((1, u'Total atendido'), (2, u'Nuevo'), (3, 'En seguimiento'), (4, u'En abandono'), (5, u'Con diagnóstico favorable'))

class CasoAtendido(models.Model):
    informe = models.ForeignKey(Informe)
    tipo_caso = models.IntegerField(choices=TIPOS_CASOS, verbose_name=u'Tipo de caso')
    situacion_caso = models.IntegerField(choices=SITUACION_CASOS, verbose_name=u'Situación del caso')
    cantidad = models.IntegerField()
    
    def __unicode__(self):        
        return u'%s - %s' % (self.informe, self.id)
    
    class Meta:
        verbose_name_plural = u'Casos Atendidos'

TIPO_DENUNCIA = ((1, u'Violencia'), (2, u'Pensión alimenticia'), (3, u'Violencia intrafamiliar'), (4, u'Delitos sexuales'))
INSTANCIA_ADMINISTRA = ((1, u'Policía Nacional/Comisaría de la mujer'),
                        (2, u'Fiscalía'), 
                        (3, u'Juzgado'))
SITUACION_DENUNCIA = ((1, u'Recibidas'), (2, u'Atendidas'), (3, u'Que concluye con sanción penal'), (4, u'Con sentencia favorable'))

class DenunciaInterpuesta(models.Model):
    informe = models.ForeignKey(Informe)
    tipo_denuncia = models.IntegerField(choices=TIPO_DENUNCIA, verbose_name=u'Tipo de denuncia')
    instancia_administra = models.IntegerField(choices=INSTANCIA_ADMINISTRA, verbose_name=u'Instancia que administra justicia')
    situacion_denuncia = models.IntegerField(choices=SITUACION_DENUNCIA, verbose_name=u'Situación de la denuncia')
    
    def __unicode__(self):        
        return u'%s - %s' % (self.informe, self.id)
    
    class Meta:
        verbose_name_plural = u'Denuncias Interpuestas'
        
ORGANIZACION_CHOICE = ((1, u'Oyanka'), (2, u'INPRHU'), (3, u'Fundación entre Mujeres'))
TIPO_POBLACION_ATENCION = ((1, u'Mujeres'), (2, u'Niños'), (3, u'Niñas'), (4, u'Adolescentes'))
SI_NO_SIMPLE = ((1, 'Si'), (2, 'No'))

class AtencionMujer(models.Model):
    informe = models.ForeignKey(Informe)
    organizacion = models.IntegerField(choices=ORGANIZACION_CHOICE)
    tipo_poblacion = models.IntegerField(choices=TIPO_POBLACION_ATENCION)
    plan_vida = models.IntegerField(choices=SI_NO_SIMPLE)        
    
    def __unicode__(self):        
        return u'%s - %s' % (self.informe, self.id)
    
    class Meta:
        verbose_name = u'Atención a Mujeres'
        verbose_name_plural = u'Atenciones a Mujeres'

TIPO_REFERENCIA = ((1, u'Referencia realizada por la organización'), (2, u'Contrareferencia recibida por la organización'))
INSTANCIA_PUBLICA = ((1, u'Policía Nacional/Comisaría de la mujer'), 
                        (2, u'Ministerio de la familia'), 
                        (3, u'Medicinal Legal'), 
                        (4, u'Ministerio público y fiscalía'),
                        (5, u'Juzgado'))

SI_NO_REF = ((1, u'Si'), (2, u'No'), (3, u'No sabe'))

class ReferenciaContraReferencia(models.Model):
    informe = models.ForeignKey(Informe)
    instancia = models.IntegerField(choices=INSTANCIA_PUBLICA, verbose_name=u'Instancia pública')
    tipo_referencia = models.IntegerField(choices=TIPO_REFERENCIA, verbose_name=u'Tipo de referencia')
    atendido_personal_pertinente = models.IntegerField(choices=SI_NO_REF, verbose_name=u'Atendido por personal pertinente')
    
    def __unicode__(self):        
        return u'%s - %s' % (self.informe, self.id)
    
    class Meta:
        verbose_name = u'Referencia y Contrareferencia'
        verbose_name_plural = u'Referencias y Contrareferencias'
        
#----------------------------- Resultado 3.1 --------------------------------
A_TRAVES = ((1, u'Sistema contable'), (2, u'Manual de procedimiento'), (3, u'Archivo y resguardo de información'),
            (4, u'Seguimiento al presupuesto'), (5, u'Estado financiero'), (6, u'Documentos legales actualizados'))

class CapacidadAdmitiva(models.Model):
    informe = models.ForeignKey(Informe)
    ha_mejorado = models.IntegerField(choices=SI_NO_SIMPLE)
    atraves = models.IntegerField(choices=A_TRAVES, blank=True, null=True)
    
    def __unicode__(self):        
        return u'%s - %s' % (self.informe, self.id)
    
    class Meta:
        verbose_name = u'Capacidad Administrativa'
        verbose_name_plural = u'Capacidad Administrativa'

MANERA = ((1, u'Enfoque temático'), (2, u'Sistema de monitoreo'),
          (3, u'Acceso de información'), (4, u'Uso de información'))

class MedirReportar(models.Model):
    informe = models.ForeignKey(Informe)
    ha_mejorado = models.IntegerField(choices=SI_NO_SIMPLE)
    manera = models.IntegerField(choices=MANERA)
    
    def __unicode__(self):        
        return u'%s - %s' % (self.informe, self.id)
    
    class Meta:
        verbose_name = u'Medir y Reportar'
        verbose_name_plural = u'Medir y Reportar'

MANERA_PLAN = ((1, u'Para la gestión en desarrollo del proyecto'),
               (2, u'Para la consecución y ejecución de recursos'),
               (3, u'Para la infromacion y comunicación'),
               (4, u'Como visión estratégica'))

class PlanEstrategico(models.Model):
    informe = models.ForeignKey(Informe)
    utiliza_plan = models.IntegerField(choices=SI_NO_SIMPLE)
    manera = models.IntegerField(choices=MANERA_PLAN)
    
    def __unicode__(self):        
        return u'%s - %s' % (self.informe, self.id)
    
    class Meta:
        verbose_name = u'Plan Estratégico'
        verbose_name_plural = u'Plan Estratégico'
                   









   
    


    
    
    
    
