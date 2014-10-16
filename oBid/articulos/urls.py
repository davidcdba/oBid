from django.conf.urls import patterns, url
from articulos import views

urlpatterns = patterns('',
                       # Users
					url(r'^(?P<categoria_id>\d+)$', views.articulosList, name='list'),
					url(r'^detalle/(?P<articulo_id>\d+)$', views.articuloVisor.as_view(), name='list'),
					url(r'^compra/(?P<articulo_id>\d+)$', views.comprar, name='list'),
                    url(r'^nuevo$', views.nuevoArticulo, name='nuevo'),
                    url(r'^misCompras$', views.listCompras, name='list'),

)
