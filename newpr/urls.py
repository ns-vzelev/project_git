from django.conf.urls.defaults import *
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'newpr.views.index'),
    (r'^find/+(?P<fn>[^/]*)\+(?P<path>.*)', 'newpr.views.fin'),
    (r'^dir/+(?P<path>.*)', 'newpr.views.Dir'),
    (r'^textfiles/+(?P<path>/.*)$', 'newpr.views.textfiles'),
    (r'^db/$', 'newpr.views.proba'),
    (r'^Form/$', 'newpr.views.form'),
    (r'^add?','newpr.modClass.store.person'),
    (r'^delete/+(?P<ident>[0-9]*)$','newpr.modClass.store.delete'),
    (r'^upload/$', 'newpr.views.upload'),
    (r'^uploadFile/$', 'newpr.uploadFile.uploadFile'),
    (r'^admin/', include(admin.site.urls)),
    (r'.*','newpr.views.Error')
)

