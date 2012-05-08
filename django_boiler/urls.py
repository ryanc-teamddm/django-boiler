from django.conf.urls import patterns, include, url
from django.contrib import admin
from feincms.views.base import handler
import os

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_boiler.views.home', name='home'),
    # url(r'^django_boiler/', include('django_boiler.foo.urls')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(os.path.dirname(__file__), '../')}),
    url(r'^$', handler, name='feincms_home'), 
	url(r'^(.*)/$', handler, name='feincms_handler'),
)