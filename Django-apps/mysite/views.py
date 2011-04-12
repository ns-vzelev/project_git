from django.template import Context, loader
from django.http import HttpResponse
import find2, settings, listDir, os
def index(request):
	ht = HttpResponse()
	ht.write('<a href= '+'"'+"dir/"+'">Click here for app - DIR</a>')
	return ht

def fin(request,path,fn):
	root = settings.Velly_Root	
	res = find2.findReal(root+path,fn)
	ht = HttpResponse()
	for el in res:
		if el != "\n":
			ht.write(el)
		else: ht.write("<br>")
	ht.write("<a href = ""http://abv.bg"">abv.bg</a>")
	ht.flush()
	return ht

def Dir(request, path):
	root = settings.Velly_Root
	p = os.path.join(root,path)
	res = listDir.execute(p, settings.temps[0], settings.temps[1])
	c = Context({
        	'STATIC_URL': settings.STATIC_URL
    	})
	f = open(settings.TEMPLATE_DIRS+"ind.html", "w")
	f.write(res)
	f.flush()
	f.close()
	t = loader.get_template(settings.TEMPLATE_DIRS+"ind.html")
	return HttpResponse(t.render(c))

def textfiles(request, path):
	root = settings.Velly_Root
	p = root+path
	f = open(p,"r")
	res = '<INPUT TYPE="button" VALUE="Back" onClick="history.go(-1);"><br><br>'
	l = f.readlines()
	f.close()
	for el in l:
		el = el.replace("	", "      ")
		el = el.replace("<", "&#60;")
		el = el.replace(">",	"&#62;")
		res += el.replace(" ", "&nbsp;")+"<br>"
	return HttpResponse(res)
def data(request, key):
	return HttpResponse()
	
