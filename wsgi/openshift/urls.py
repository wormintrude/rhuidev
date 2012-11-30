from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'openshift.views.home', name='home'),
    # url(r'^openshift/', include('openshift.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),

    url(r'^report/', 'openshift.views.report', name='report'),
    url(r'^rhui_xmlrpc_server/', 'openshift.views.xmlrpc_server', name='xmlrpc_server'),
#    url(r'^rhui_xmlrpc_server/', 'openshift.views.rhui_xmlrpc_handler', name='rhui_xmlrpc_handler'),
    url(r'^db_test/', 'openshift.views.rhui_db_test', name='rhui_db_test'),
    url(r'^db_write/', 'openshift.views.rhui_db_write_test', name='rhui_db_write_test'),
    url(r'^db_read/', 'openshift.views.rhui_db_read_test', name='rhui_db_read_test'),

)
