from django.conf.urls import patterns, include, url
## AVISO ## Linea descomentada, activa el acceso al panel de administracion
from django.contrib import admin 
## AVISO ## Linea descomentada, activa el acceso al panel de administracion
admin.autodiscover()

## Linea que importa la clase TemplateView (Usada para acceder a los templates)
from django.views.generic import TemplateView 
from django.conf import settings ## Linea que importa la clase setting (Usada para el contenido MEDIA y STATIC)
from django.conf.urls.static import static ## Linea que importa la clase static (Usada para el contenido MEDIA y STATIC)
from subasta import views # importa todas las vista de la apicacion subasta

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oBid.views.home', name='home'),
    # url(r'^oBid/', include('oBid.foo.urls')),
    
     url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
     url(r'^categorias/list$', views.categoriaList, name='categoriaList'),
   ## AVISO ## Linea descomentada, activa el acceso a la documentacion del panel de administracion
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

  ## AVISO ## Linea descomentada, activa el acceso al panel de administracion
     url(r'^admin/', include(admin.site.urls)), 
     ## Activa el acceso al contenido MEDIA y STATIC

     #una linea para cada aplicacion
    url(r'^usuarios/', include('usuarios.urls', namespace='usuarios')),
    url(r'^articulos/', include('articulos.urls', namespace='articulos')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
