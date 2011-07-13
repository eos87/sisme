# -*- coding: UTF-8 -*-

def global_vars(request):
    if request.user.is_authenticated():
        username = request.user.username
        if username == 'equipofed':
            user_org = 'FED'
        else:
            user_org = request.user.organizacion_set.all().order_by('?')[0].nombre_corto                        
    else:
        username = u'Invitado'
        user_org = u'Ninguna'    
    
    dicc = {
        'username': username,
        'user_org': user_org,        
    }
    return dicc