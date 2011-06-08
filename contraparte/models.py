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

class Informe(models.Model):
    organizacion = models.ForeignKey(Organizacion)
    proyecto = models.ForeignKey(Proyecto)
    anio_desde = models.IntegerField(choices=YEARS, verbose_name=u'Año')
    mes_desde = models.IntegerField(choices=MESES, verbose_name=u'Mes')
    anio_hasta = models.IntegerField(choices=YEARS, verbose_name=u'Año')
    mes_hasta = models.IntegerField(choices=MESES, verbose_name=u'Mes')
        
    class Meta:
        verbose_name_plural = u'Informes'        
    
