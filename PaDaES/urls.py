from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'PaDaES.qxgui.views.index'),
    # url(r'^RPC2$', 'rpc4django.views.serve_rpc_request'),

    # Examples:
    # url(r'^$', 'PaDaES.views.home', name='home'),
    # url(r'^PaDaES/', include('PaDaES.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
