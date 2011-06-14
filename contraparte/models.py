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
    tipo_comision = models.ForeignKey(Comision)
    tipo_accion = models.IntegerField(choices=ACCIONES)
    estado = models.IntegerField(choices=ESTADO_ACCION, verbose_name=u'Situación de la acción')
    ambito = models.IntegerField(choices=AMBITO, verbose_name=u'Ámbito territorial')
    
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
    
    verbose_name = u'Observatorio'
    verbose_name_plural = u'Observatorios'
        




    
    
    
    