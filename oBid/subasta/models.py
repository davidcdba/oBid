from django.db import models
 ## EXPLICACION ## Se importa la clase (modelo) User de los modelos propios de Django
from usuarios.models import Usuario
from articulos.models import Articulo
import datetime
# Create your models here.

class Puja(models.Model):
	tiempo=(datetime.date.today()+datetime.timedelta(days=0))
	cantidad = models.CharField(max_length=5)

	fechaPuja = models.DateField(default=tiempo,null=True,blank=True)
	#hora= models.TimeField()
	articulo = models.ForeignKey(Articulo)
	usuario= models.ForeignKey(Usuario)
	def __unicode__(self):
		return unicode(self.fechaPuja)
class Compra(models.Model):
	tiempo=(datetime.date.today()+datetime.timedelta(days=0))
	fecha=models.DateField(blank=True,default=tiempo)
	articulo = models.ForeignKey(Articulo)
	usuario= models.ForeignKey(Usuario)
	def __unicode__(self):
		return unicode(self.fecha)
class Valoracion(models.Model):
		articulo = models.ForeignKey(Articulo)
		usuarioEmisor= models.ForeignKey(Usuario, related_name='emisor')
		usuarioReceptor= models.ForeignKey(Usuario, related_name='receptor')
		comentario = models.TextField()
	
		estrellas =  models.IntegerField(max_length=1)
		def __unicode__(self):
			return self.pk

class Mensaje(models.Model):
		#articulo = models.ForeignKey(Articulo)
		usuarioEmisor= models.ForeignKey(Usuario, related_name='emisorMensaje')
		usuarioReceptor= models.ForeignKey(Usuario, related_name='receptorMensaje')
		mensaje = models.TextField()
		asunto = models.CharField(max_length=100)
		
		def __unicode__(self):
			return self.asunto