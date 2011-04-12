from django.template import Context, loader
from django.http import HttpResponse
from django.db import models
from modClass import tableGenerator
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

import find2, settings, listDir, os, uploadFile
import probadb
def index(request):
	ht = HttpResponse()
	ht.write('<a href= '+'"'+"dir/"+'">Click here for app - DIR </a><br>')
	ht.write('<a href = "/Form/">Form </a><br>')
	ht.write('<a href = "/upload/">Upload files</a>')
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
	try:
		f = open(p,"r")
	except IOError:
		return HttpResponse("Access denied")
	res = '<INPUT TYPE="button" VALUE="Back" onClick="history.go(-1);"><br><br>'
	l = f.readlines()
	f.close()
	for el in l:
		el = el.replace("	", "      ")
		el = el.replace("<", "&#60;")
		el = el.replace(">",	"&#62;")
		res += el.replace(" ", "&nbsp;")+"<br>"
	return HttpResponse(res)

def proba(request):
	 return HttpResponse(probadb.delete())

def form(request):
	try:
	     f = open(settings.STATICFILES_DIRS[0]+'/index.html','r')
	     f1 = open(settings.temps[1],'r')
	     t = f1.read()
	     res = f.read()
	     res += '<br><a href ="/dir/">DIR</a>'
	     f.close()
	     f1.close()
	     return HttpResponse(res.replace("#$$$list$$$#",tableGenerator.generate('Person')))
	except IOError:
		 return HttpResponse("Form template does not exist<br>"+settings.STATICFILES_DIRS[0]+'/index.html')
	   
def Error(request):
	return HttpResponse('<html><head><META HTTP-EQUIV="REFRESH" CONTENT="1;URL=/"></head>Error 404</html>')  	

def upload(request):
	try:
		res = listDir.execute(settings.UPLOAD_PATH,settings.temps[3],settings.temps[1])
		f = open(settings.TEMPLATE_DIRS+"/t.html", 'w')
		f.write(res)
		f.close()
		return render_to_response(settings.TEMPLATE_DIRS+"/t.html", Context(csrf(request)))
	except IOError:
		return "Cannot open template upload.html"
