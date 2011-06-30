# -*- coding: UTF-8 -*-
from django import forms
from django.forms import ModelForm
from sisme.fed.models import *
from sisme.fed.forms import ANIOS
import datetime


MONTH_CHOICES = (('', 'Mes'),
                 (1, 'Enero'), (2, 'Febrero'),
                 (3, 'Marzo'), (4, 'Abril'),
                 (5, 'Mayo'), (6, 'Junio'),
                 (7, 'Julio'), (8, 'Agosto'),
                 (9, 'Septiembre'), (10, 'Octubre'),
                 (11, 'Noviembre'), (12, 'Diciembre'))

ANIOS_CHOICE = (('', u'Año'), (2009, 2009), (2010, 2010), (2011, 2011))

class InfluenciaForm(forms.Form):
    modalidad = forms.MultipleChoiceField(choices=MODALIDAD_CHOICE, label='Modalidad de apoyo', required=False)
    organizacion = forms.ModelMultipleChoiceField(queryset=Organizacion.objects.all(), label='Organizaciones', required=False)
    resultado = forms.ModelMultipleChoiceField(queryset=Resultado.objects.all(), label='Resultados', required=False)
    mes_inicio = forms.ChoiceField(choices=MONTH_CHOICES, error_messages={'required': 'Seleccione un mes'})
    anio_inicio = forms.ChoiceField(choices=ANIOS_CHOICE, error_messages={'required': u'Seleccione un año'})
    mes_fin = forms.ChoiceField(choices=MONTH_CHOICES, error_messages={'required': 'Seleccione un mes'})
    anio_fin = forms.ChoiceField(choices=ANIOS_CHOICE, error_messages={'required': u'Seleccione un año'})