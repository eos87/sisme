# -*- coding: UTF-8 -*-
from django.contrib import admin
from models import *

class InformeAdmin(admin.ModelAdmin):
    add_form_template = 'admin/contraparte/informe/add_template.html'
    fieldsets = [
        (None, {'fields': ['organizacion', 'proyecto']}),
        (u'Inicio de período', {'fields': [('anio_desde', 'mes_desde'),]}),
        (u'Fin de período', {'fields': [('anio_hasta', 'mes_hasta')]}),        
    ]    

admin.site.register(Informe, InformeAdmin)