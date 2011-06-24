# -*- coding: UTF-8 -*-
from django import forms

ANIOS = ((0, 'Todos'), (2009, 2009), (2010, 2010), (2011, 2011))

class GralForm(forms.Form):
    year = forms.ChoiceField(choices=ANIOS, label=u'Año')