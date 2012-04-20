from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_boiler.views.home', name='home'),
    # url(r'^django_boiler/', include('django_boiler.foo.urls')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)
