from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', TemplateView.as_view(template_name="numbers.html")),
	#(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'numbers.html'}),
	(r'^gna/', include('simuapps.gna.urls')),
	(r'^gva/', include('simuapps.gva.urls')),
    (r'^model/', include('simuapps.model.urls')),
    # Examples:
    # url(r'^$', 'simulaproj.views.home', name='home'),
    # url(r'^simulaproj/', include('simulaproj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
