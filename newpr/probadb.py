import settings
from modClass import models
def proba():
    p = models.Person(first_name = 'Dido', last_name = 'Bogiii')
    p.save()
    return str(p.first_name+" "+p.last_name+" "+str(p.id))
def delete():
    p = models.Person.objects.all()
    r = ""
    for el in p:
        r += el.first_name+"   "+str(el.id)+"<br>"
    return r 
