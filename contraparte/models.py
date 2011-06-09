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
    ambito = models.IntegerField(choices=AMBITO)
    
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
    
    
    
    
    
    
    
    
    
    
    