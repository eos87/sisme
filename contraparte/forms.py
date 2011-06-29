# -*- coding: UTF-8 -*-
from django import forms
from django.forms import ModelForm
from sisme.fed.models import *
import datetime

MONTH_CHOICES = ((1, 'Enero'), (2, 'Febrero'),
                 (3, 'Marzo'), (4, 'Abril'),
                 (5, 'Mayo'), (6, 'Junio'),
                 (7, 'Julio'), (8, 'Agosto'),
                 (9, 'Septiembre'), (10, 'Octubre'),
                 (11, 'Noviembre'), (12, 'Diciembre'))

class InfluenciaForm(forms.Form):
    tipo = forms.MultipleChoiceField(choices=MODALIDAD_CHOICE, label='Modalidad de apoyo')
    organizacion = forms.ModelMultipleChoiceField(queryset=Organizacion.objects.all(), label='Organizaciones')
    resultado = forms.ModelMultipleChoiceField(queryset=Resultado.objects.all(), label='Resultados')
    mes_inicio = forms.ChoiceField(choices=MONTH_CHOICES)
    #periodo = forms.MultipleChoiceField(choices=CHOICE_PERIODO, label='Período')
    #anio = forms.ChoiceField(choices=CHOICE_ANIO, label='Año')