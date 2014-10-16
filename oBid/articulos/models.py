from django.db import models
from usuarios.models import Usuario
import datetime

#contiene las categorias del sistema
class Categoria(models.Model):
	nombre = models.CharField(max_length=100,unique=True)
	descripcion= models.TextField()
	#sube una imagen upload_to idenifica la carpeta
	imagen = models.ImageField(upload_to = 'categorias', verbose_name = 'Imagen') 
	def __unicode__(self):
		return self.nombre #define el campo que se mostrara  como identificador de la clase

class Articulo(models.Model):
	tiempoFin=(datetime.date.today()+datetime.timedelta(days=7))
	titulo = models.CharField(max_length=100,unique=True)
	descripcion= models.TextField()
	fechaInicio = models.DateField(default=datetime.date.today)
	fechaFin = models.DateField(default=tiempoFin)	
	pujaMinima= models.IntegerField(default=0)
	gastosEnvio= models.IntegerField(default=0)
	TIPOVENTA = ( ## tipos de ventas
        	('SB', 'Subasta'),
        	('CD', 'Compra directa'),
        	
    	)
	## Tamano Maximo: 2, Opciones disponibles de TIPOVENTA, valor pordefecto SB
	tipoVenta = models.CharField(max_length=2,choices=TIPOVENTA,default='SB') 
	TIPOPAGO = ( ## tipos de ventas
        	('PA', 'Paypal'),
        	('TB', 'Transferencia bancaria'),
        	
    	)
	imagen= models.ImageField(upload_to = 'articulos', verbose_name = 'Imagen', default='articulos/default.png') 
	## Tamano Maximo: 2, Opciones disponibles de TIPOPAGO, valor pordefecto SB
	formaPago = models.CharField(max_length=2,choices=TIPOPAGO,default='PA') 
	categoria = models.ForeignKey(Categoria,related_name='categoriaArticulo')#relacion con categorias
	Usuario = models.ForeignKey(Usuario)#relacion con categorias
	def __unicode__(self):
		return self.titulo