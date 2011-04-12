import settings, models
def generate(Classname):
    try:
        p = models.Person.objects.all()
        res = ('<table border = "1">')
        f = open(settings.temps[2])
        temp = f.read()
        f.close()
        for el in p:
            r = temp.replace("#$$$fn$$$#", el.first_name)
            r = r.replace("#$$$fs$$$#", el.last_name)
            delTag = '<a href = "/delete/'+str(el.id)+'">Delete</a>'
            r = r.replace("#$$$del$$$#", delTag)
            res += r
        return res+ '</table><br>' 
    except IOError:
        return 'Template error'