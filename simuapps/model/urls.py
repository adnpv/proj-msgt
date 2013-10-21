from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
#from event.views import HelloTemplate#agregar el class view! desde nuestras vistas
urlpatterns= patterns('simuapps.model.views',
	url(r'^$',TemplateView.as_view(template_name="models_home.html")),
	url(r'^valores_procesos/$','process'),
	url(r'^valores_arribos/$','arrib'),
	
	# url(r'^uhome/$','uhome'),
	# url(r'^newacc/$','crear_cuenta'),
	# url(r'^newev/$','crear_evento'),
	# url(r'^contact/$','contact'),

	# url(r'^interact/(?P<event_id>\d+)/$','interacc'),
	# url(r'^eventosh/$','mis_eventos'),
	# url(r'^serv/$','servicio'),
	
	# url(r'^login/$','login'),
	# url(r'^entradas/$','mis_entradas'),
	# url(r'^comprar/$','comprar'),
	# url(r'^get/(?P<event_id>\d+)/$','event'),

	#url(r'^language/(?P<language>[a-z\-]+)/$','event.views.language'),
)
