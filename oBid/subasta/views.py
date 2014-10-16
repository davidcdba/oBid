# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from articulos.models import Categoria

def categoriaList(request):

	list= Categoria.objects.all().order_by("nombre") #obtiene todos y los ordena por nombre

	context = {'categoriaList' : list} ## Se le anade un contexto a la lista para poder tratar los datos en el template
	return render(request, 'categorias/list.html', context) ## Se devuelve la informacion al template

