from django.shortcuts import render_to_response
from django.template.context import RequestContext

def save_as_xls(request):
    tabla = request.POST['tabla']
    print tabla
    response = render_to_response('xls.html', {'tabla': tabla, })
    response['Content-Disposition'] = 'attachment; filename=tabla.xls'
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response