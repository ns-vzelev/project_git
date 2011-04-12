from django.conf.urls.defaults import *
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'mysite.views.index'),
    (r'^find/+(?P<fn>[^/]*)\+(?P<path>.*)', 'mysite.views.fin'),
    (r'^dir/+(?P<path>.*)', 'mysite.views.Dir'),
    (r'^textfiles/+(?P<path>/.*)$', 'mysite.views.textfiles'),
    (r'^admin/', include(admin.site.urls))
)

