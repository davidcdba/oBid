#encoding: utf-8

from django.forms import ModelForm # Importa el modelo de formularios
from articulos.models import Articulo
from subasta.models import Puja, Compra
class NuevoArticulo(ModelForm):
	class Meta:
	        model = Articulo
	        fields = ('titulo','descripcion','pujaMinima','gastosEnvio','categoria','formaPago','tipoVenta','imagen')#campos que deben aparecer en un formulario
	def _init_(self, *args, **kwargs):
		super(ModelForm,self).__init__(*args,**kwargs)
		self.fields['titulo'].label='Nombre' # Se le anade un sobrenombre a los campos de nuestro modelo
		self.fields['descripcion'].label='descripcion'
		
		
		self.fields['pujaMinima'].label='Puja o precio de venta Minimo'
		self.fields['gastosEnvio'].label='Gastos de envio'
		self.fields['categoria'].label='Categoria'
		self.fields['formaPago'].label='forma de pago'
		self.fields['tipoVenta'].label = "Venta"
		
		self.fields['imagen'].label = "Imagen de Articulo"
		self.fields['imagen'].widget.attrs.update({'class' : 'file'})
		self.fields['imagen'].widget.attrs.update({'accept' : 'image/*'})

class addBid(ModelForm):
	class Meta:
		model= Puja
		fields= ('cantidad',)
	def _init_(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args,**kwargs)
		self.fields['cantidad'].label='Pujar por '
		
class nuevaCompra(ModelForm):
	class Meta:
		model= Compra
		fields= ('fecha',)
	def _init_(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args,**kwargs)
		self.fields['fecha'].label='Estas deacuerdo con comprar el producto '

		