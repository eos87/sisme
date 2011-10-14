# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
from sisme.lugar.models import Municipio
from sisme.files import *
from sisme.thumbs import ImageWithThumbsField
import datetime

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^sisme\.thumbs\.ImageWithThumbsField"])

class Organizacion(models.Model):
    user = models.ForeignKey(User, verbose_name='Usuario')
    nombre = models.CharField(max_length=200)
    nombre_corto = models.CharField(max_length=25)
    #codigo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=250, blank=True, default='')
    fecha = models.DateField(default=datetime.date.today(), blank=True, verbose_name=u'Fecha de Constitución')
    no_mingob = models.CharField(max_length=50, blank=True, default='', verbose_name=u'No. perpetuo del MINGOB')
    no_ruc = models.CharField(max_length=50, blank=True, default='', verbose_name=u'No. RUC')
    no_inss = models.CharField(max_length=50, blank=True, default='', verbose_name=u'No. patronal del INSS')
    representante_legal = models.CharField(max_length=120, blank=True, default='')
    telefono_1 = models.CharField(max_length=15, blank=True, default='')
    telefono_2 = models.CharField(max_length=15, blank=True, default='')
    email = models.EmailField(blank=True, default='email@example.com')
    contacto = models.CharField(max_length=120, blank=True, default='', verbose_name=u'Persona de contacto del proyecto')
    telefono_contacto = models.CharField(max_length=15, blank=True, default='', verbose_name=u'Teléfono del contacto')
    sitio_web = models.URLField(blank=True, default='www.example.com', verify_exists=False)
    obj_gral = models.TextField(blank=True, default='', verbose_name='Objetivo General')
    estrategias = models.TextField(blank=True, default='', verbose_name=u'Líneas estratégicas')
    antecedentes = models.TextField(blank=True, default='')
    logo = ImageWithThumbsField(upload_to=get_file_path, sizes=((122, 91), (160, 75)), blank=True, null=True, help_text=u'Logo de la organizacion')
    
    fileDir = 'logos'
    
    def __unicode__(self):
        return u'%s' % self.nombre_corto
    
    class Meta:
        verbose_name = u'Organización'
        verbose_name_plural = u'Organizaciones'

class Donante(models.Model):
    nombre = models.CharField(max_length=200)
    nombre_corto = models.CharField(max_length=25)
    
    def __unicode__(self):
        return u'%s' % self.nombre_corto
    
    class Meta:        
        verbose_name_plural = u'Donantes'
        
class Tema(models.Model):    
    nombre = models.CharField(max_length=100)    
    
    def __unicode__(self):
        return u'%s' % self.nombre
    
    class Meta:
        verbose_name = u'Tema de FED'        
        verbose_name_plural = u'Temas del FED'

class Resultado(models.Model):
    nombre_corto = models.CharField(max_length=35)
    descripcion = models.TextField()
    codigo = models.IntegerField()
    
    def __unicode__(self):
        return u'%s' % self.nombre_corto
    
    class Meta:        
        verbose_name_plural = 'Resultados'


MODALIDAD_CHOICE = ((1, u'Apoyo programático'),
               (2, u'Convocatoria pública'),               
               (3, u'Pequeños proyectos'),
               (4, u'Actividades puntuales'),
               (5, u'Acciones de emergencia'),
               (6, u'Estrategias con grupos priorizados'))

COBERTURA = ((1, 'Municipal'), (2, 'Departamental'), (3, 'Nacional'))

class Proyecto(models.Model):    
    organizacion = models.ForeignKey(Organizacion)
    codigo = models.CharField(max_length=100, verbose_name=u'Código', unique=True)
    nombre = models.TextField()
    modalidad = models.IntegerField(choices=MODALIDAD_CHOICE, verbose_name=u'Modalidad de apoyo')
    cobertura = models.IntegerField(choices=COBERTURA, verbose_name=u'Area de Cobertura')
    fecha_inicio = models.DateField(default=datetime.date.today(), verbose_name=u'Fecha de Inicio')
    fecha_fin = models.DateField(default=datetime.date.today(), verbose_name=u'Fecha de Finalización')
    monto_fed = models.DecimalField('Monto aprobado por FED', blank=True, null=True, decimal_places=2, max_digits=30)    
    monto_contrapartida = models.DecimalField('Monto contrapartida local', blank=True, null=True, decimal_places=2, max_digits=30)
    monto_otros = models.DecimalField('Monto otros donantes', blank=True, null=True, decimal_places=2, max_digits=30)
    otros_donantes = models.ManyToManyField(Donante, blank=True, null=True)    
    resultados = models.ManyToManyField(Resultado, blank=True, null=True)
    
    def __unicode__(self):
        return u'%s - %s' % (self.organizacion.nombre_corto, self.codigo)
    
    def get_monto_total(self):
        return self.monto_fed + self.monto_contrapartida + self.monto_otros
    
    class Meta:
        verbose_name_plural = u'Proyectos'
        
class TemaTrabajo(models.Model):
    proyecto = models.ForeignKey(Proyecto)
    municipio = models.ManyToManyField(Municipio)
    tema = models.ManyToManyField(Tema)
    
    def __unicode__(self):
        return u'%s - %s' % (self.proyecto.codigo, self.id)
    
    class Meta:
        verbose_name = u'Tema de trabajo'
        verbose_name_plural = u'Temas de trabajo'
    
GRUPO_ETAREO = ((1, u'Menor de 12 años'), (2, u'De 12 a 18 años'),
                (3, u'De 19 a 27 años'), (4, u'De 28 en adelante'))    

class PoblacionMetaBase(models.Model):
    proyecto = models.ForeignKey(Proyecto)
    grupo_etareo = models.IntegerField(choices=GRUPO_ETAREO)
    hombres = models.IntegerField()
    mujeres = models.IntegerField()
    
    def get_total(self):
        return self.hombres + self.mujeres
    
    def __unicode__(self):
        return u'%s - %s' % (self.proyecto.codigo, self.id)
             
    class Meta:
        abstract = True
        
class PoblacionMetaDirecta(PoblacionMetaBase):
    class Meta:
        verbose_name = u'Población Meta Directa'
        verbose_name_plural = u'Población Meta Directa'
    
class PoblacionMetaIndirecta(PoblacionMetaBase):
    class Meta:
        verbose_name = u'Población Meta Indirecta'
        verbose_name_plural = u'Población Meta Indirecta'
    
    
    
        
