# -*- coding: UTF-8 -*-
from django import forms
from models import Organizacion

ANIOS = ((0, 'Todos'), (2009, 2009), (2010, 2010), (2011, 2011))
ANIO_2 = ((0, u'Año'), (2010, 2010), (2011, 2011))

class GralForm(forms.Form):
    year = forms.ChoiceField(choices=ANIOS, label=u'Elegir Año')
    
class GanttForm(forms.Form):
    anio = forms.ChoiceField(choices=ANIO_2, label=u'Elegir Año')
    organizacion = forms.ModelChoiceField(queryset=Organizacion.objects.all(), empty_label='Organización')    