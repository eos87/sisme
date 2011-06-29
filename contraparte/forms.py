# -*- coding: UTF-8 -*-
from django import forms
from django.forms import ModelForm
from sisme.fed.models import *
from sisme.fed.forms import ANIOS
import datetime


MONTH_CHOICES = ((1, 'Enero'), (2, 'Febrero'),
                 (3, 'Marzo'), (4, 'Abril'),
                 (5, 'Mayo'), (6, 'Junio'),
                 (7, 'Julio'), (8, 'Agosto'),
                 (9, 'Septiembre'), (10, 'Octubre'),
                 (11, 'Noviembre'), (12, 'Diciembre'))

class InfluenciaForm(forms.Form):
    modalidad = forms.MultipleChoiceField(choices=MODALIDAD_CHOICE, label='Modalidad de apoyo')
    organizacion = forms.ModelMultipleChoiceField(queryset=Organizacion.objects.all(), label='Organizaciones')
    resultado = forms.ModelMultipleChoiceField(queryset=Resultado.objects.all(), label='Resultados')
    mes_inicio = forms.ChoiceField(choices=MONTH_CHOICES)
    anio_inicio = forms.ChoiceField(choices=ANIOS)
    mes_fin = forms.ChoiceField(choices=MONTH_CHOICES)
    anio_fin = forms.ChoiceField(choices=ANIOS)