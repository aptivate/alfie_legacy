from django.conf.urls import patterns, include, url
#from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import logframe.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myapp.views.home', name='home'),
    # url(r'^myapp/', include('myapp.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^logframe/', include(logframe.urls)),

    #This requires that static files are served from the 'static' folder.
    #The apache conf is set up to do this for you, but you will need to do it on
    #dev
    url(r'favicon.ico', RedirectView.as_view(
        url='{0}images/favicon.ico'.format(settings.STATIC_URL))),

    # LAST - redirect from root URL to the logframe app
    url(r'^$', RedirectView.as_view(url='/logframe/overview/1/')),
    # TODO: work out why the below doesn't work ...
    #url(r'^$', RedirectView.as_view(url=reverse_lazy('logframe-overview', 1))),
)
