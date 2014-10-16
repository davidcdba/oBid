from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Usuario(User):#asi se pone la erencia de la clase User
	fechaNacimiento = models.DateField()
	puntos = models.IntegerField(null=True, blank=True,default=0)
	direccion= models.CharField(max_length=200)
	cp= models.CharField(max_length=5)
	ciudad = models.CharField(max_length=200)
	nif= models.CharField(max_length=9)
	avatar= models.ImageField(upload_to = 'usuarios', verbose_name = 'Avatar', default='usuarios/default.png') 
	def __unicode__(self):
		return self.username#username es un campo definido de la clase user