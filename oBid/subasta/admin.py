## EXPLICACION ## Archivo creado para registrar las clases creadas en el modelo en la interfaz de administracion
from django.contrib import admin ## Se importa la clase Admin
from subasta.models import  Puja, Compra, Valoracion, Mensaje## Se importan las clases del modelo creado
from usuarios.models import Usuario
from articulos.models import Articulo, Categoria
## EXPLICACION ## Se registran cada una de las clases de nuestro modelo
admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Articulo)
admin.site.register(Puja)
admin.site.register(Compra)
admin.site.register(Valoracion)
admin.site.register(Mensaje)