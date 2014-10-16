from django.conf.urls import patterns, url
from usuarios import views

urlpatterns = patterns('',
                       # Users
                       #url(r'^list$', views.userList, name='list'),/
                      url(r'^nuevo$', views.usersNew, name='nuevo'),
                      url(r'^modificar$', views.editar, name='editar'),
                      url(r'^mensajes$', views.mensajes, name='mensajes'),
                      url(r'^NuevoMensaje$', views.NuevoMensaje, name='mensajes'),
                      url(r'^login$', views.userLogin, name='login'),
                      url(r'^logout$', views.userLogout, name='logout'),
)
