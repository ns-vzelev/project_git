import models, settings, tableGenerator
from django.http import HttpResponse
from django.http import HttpRequest
def person(request):
    dict = None
    if request.method == 'GET':
        dict = request.GET
    elif request.method == 'POST':
        dict = request.POST
    name = dict['Name']
    lname = dict['lName']
    if len(name) == 0 or len(lname) == 0:
        h = HttpResponse()
        h.write('Name or/and Last Name is/are incorrect<br>')
        return h
    p = models.Person(first_name = name, last_name = lname)
    try:
        p.save()
        h = HttpResponse('Data stored<br> <INPUT TYPE="button" VALUE="Back" onClick="history.go(-1);"><br>')
        h.write('<html><head><META HTTP-EQUIV="REFRESH" CONTENT="1;URL=/Form/"></head></html>')
        return h
            
    except IOError:
        return HttpResponse('Temp2.html error')

def delete(request,ident):
    p = models.Person(id = ident)
    p.delete()
    h = HttpResponse()
    h.write('<html><head><META HTTP-EQUIV="REFRESH" CONTENT="0.01;URL=/Form/"></head></html>')
    return h

    