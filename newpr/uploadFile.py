from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django import forms
import settings

def handle_uploaded_file(f):
    open(settings.UPLOAD_PATH+f.name, 'w').close()
    destination = open(settings.UPLOAD_PATH+f.name, 'w+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

def uploadFile(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'])
    return HttpResponseRedirect('/upload/')
   
   
