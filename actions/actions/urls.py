from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'actions.views.home', name='home'),
    # url(r'^actions/', include('actions.foo.urls')),
    url(r'^result/$', 'result.views.index'),
    url(r'^result/(?P<action_id>\d+)/$', 'result.views.detail'),
   
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
