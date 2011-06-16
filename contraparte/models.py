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
    anio_desde = models.IntegerField(choices=YEARS, verbose_name=u'Año')
    mes_desde = models.IntegerField(choices=MESES, verbose_name=u'Mes')
    anio_hasta = models.IntegerField(choices=YEARS, verbose_name=u'Año')
    mes_hasta = models.IntegerField(choices=MESES, verbose_name=u'Mes')
    
    def desde(self):
        return u'%s %s' % (MESES[self.mes_desde][1], self.anio_desde)
    
    def hasta(self):
        return u'%s %s' % (MESES[self.mes_hasta][1], self.anio_hasta)
    
    def __unicode__(self):
        return u'%s | Período: %s - %s' % (self.organizacion.nombre_corto, self.desde(), self.hasta())
    
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
        
class Comision(models.Model):
    nombre = models.CharField(max_length=150)
    
    def __unicode__(self):
        return '%s' % self.nombre
    
    class Meta:
        verbose_name = u'Comisión'
        verbose_name_plural = 'Comisiones'
    
class ParticipacionComision(models.Model):
    informe = models.ForeignKey(Informe)
    nombre = models.CharField(max_length=200, verbose_name='Nombre de la actividad')
    tipo_comision = models.ForeignKey(Comision)
    ambito = models.IntegerField(choices=AMBITO, verbose_name=u'Ámbito territorial')
    estado = models.IntegerField(choices=ESTADO_ACCION, verbose_name=u'Efectividad de la acción')    
    
    def __unicode__(self):
        return u'%s - %s' % (self.informe, self.id)
    
    verbose_name = u'Participación en Comisiones'
    verbose_name_plural = u'Participaciones en Comisiones'
    
ACCIONES2 = ((1, u'Campañas de televisión'), (2, u'Campañas radiales'), (3, u'Artítulos de periódicos'))

class AccionAgenda(models.Model):
    nombre = models.CharField(max_length=150)
    
    def __unicode__(self):
        return '%s' % self.nombre
    
    class Meta:
        verbose_name = u'Acción de agenda'
        verbose_name_plural = 'Acciones de agenda'

class AgendaPublica(models.Model):
    informe = models.ForeignKey(Informe)
    nombre = models.CharField(max_length=200, verbose_name='Nombre de la actividad')    
    tipo_accion = models.ForeignKey(AccionAgenda)
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
class AccionDemanda(models.Model):
    nombre = models.CharField(max_length=150)
    
    def __unicode__(self):
        return '%s' % self.nombre
    
    class Meta:
        verbose_name = u'Acción de demanda'
        verbose_name_plural = 'Acciones de demanda' 

POBLACION = ((1, u'En contra de las discriminación a personas LGBT'), 
             (2, u'En contra de la discriminación a personas discapacitadas'), 
             (3, u'En contra de la discriminación a personas con VIH'), 
             (4, u'En contra de la discriminación por etnias'))

class DemandaJusticia(models.Model):
    informe = models.ForeignKey(Informe)
    nombre = models.CharField(max_length=200, verbose_name='Nombre de la actividad')
    tipo_accion = models.ForeignKey(AccionDemanda)
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
                     (4, u'Intercambios de experiencias'))

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
    tipo_poblacion = models.IntegerField(choices=TIPO_POBLACION2)
    segmento_poblacional = models.IntegerField(choices=SEGMENTO_POBLACIONAL)
    hombres = models.IntegerField('No. de participantes hombres')
    mujeres = models.IntegerField('No. de participantes mujeres')
    
    def __unicode__(self):
        return u'%s - %s' % (self.informe, self.id)
    
    class Meta:
        verbose_name = u'Posee información'
        verbose_name_plural = u'Poseen Información'
    
class RecibenInfo(models.Model):
    informe = models.ForeignKey(Informe)
    nombre = models.CharField(max_length=200, verbose_name='Nombre de la actividad')
    tipo_accion = models.IntegerField(choices=ACCION_POSEE_INFO)    
    tipo_poblacion = models.IntegerField(choices=TIPO_POBLACION2)
    segmento_poblacional = models.IntegerField(choices=SEGMENTO_POBLACIONAL)
    hombres = models.IntegerField('No. de participantes hombres')
    mujeres = models.IntegerField('No. de participantes mujeres')
    
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
    tipo_poblacion = models.IntegerField(choices=TIPO_POBLACION2)
    segmento_poblacional = models.IntegerField(choices=SEGMENTO_POBLACIONAL)
    hombres = models.IntegerField('No. de participantes hombres')
    mujeres = models.IntegerField('No. de participantes mujeres')
    
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
 
    








    
    
    


    
    
    
    