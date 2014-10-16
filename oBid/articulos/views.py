#encoding: utf-8
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from articulos.forms import NuevoArticulo, addBid, nuevaCompra
from usuarios.models import Usuario
from articulos.models import Articulo
from subasta.models import Puja,Compra
import datetime
from django.views.generic.base import View

# Create your views here.


def nuevoArticulo(request):
    # if (request.user.is_superuser and request.user.is_staff):
    if request.method == 'POST':
        # Optención del usuario activo
        userActive = Usuario.objects.get(pk=request.user.id) # Obtiene el el usuario usando el id obtenido desde la sesión

        # Can use standard form
        # form = UserCreationForm(request.POST)
        # Or customize it
        form = NuevoArticulo(request.POST, request.FILES)
        if form.is_valid():
            newArticle = form.save(commit=False)
            newArticle.Usuario = userActive
            newArticle.save()
            
            return redirect('/')
    else:
        # form = UserCreationForm()
        form = NuevoArticulo()
    tiempoFin=datetime.date.today()+datetime.timedelta(days=7)
    context = {'form':form, 'tiempoFin': tiempoFin}
    return render(request, 'articulos/nuevo.html',  context)

def articulosList(request, categoria_id):
    tiempo=datetime.date.today()+datetime.timedelta(days=0)
    Articulos =Articulo.objects.filter(categoria = categoria_id).order_by('-fechaFin')
    #list = Articulo.objects.all() ## Obtiene todos los elementos de la clase Articulo y los almacena en una lista llamada list
    context = {'Articulos' : Articulos,'tiempo': tiempo} ## Se le anade un contexto a la lista y la clase para poder tratar los datos en el template
    return render(request, 'articulos/list.html', context) ## Se devuelve la informacion al template
class articuloVisor(View):
    template_name = 'articulos/detalleArticulo.html'
    form_class=addBid
    def get(self, request, *args, **kwargs):
        tiempo=datetime.date.today()+datetime.timedelta(days=0)
        id = self.kwargs['articulo_id']
        articulo = get_object_or_404(Articulo, pk=id)#obtiene el articulo actual
        form= self.form_class
        try:
            pujarlist=Puja.objects.filter(articulo=articulo).order_by('cantidad')
            puja=-1
            
        except Exception:
          
            puja=0
        if puja==-1:
            return render(request, self.template_name, {'form':form,'articulo':articulo, 'tiempo': tiempo,'puja':puja,'pujarlist':pujarlist})
        else:
            return render(request, self.template_name, {'form':form,'articulo':articulo, 'tiempo': tiempo,'puja':puja})
     
    def post(self, request, *args, **kwargs):
      form = self.form_class(request.POST)  
      if form.is_valid():
        id = self.kwargs['articulo_id']#optiene el parametro pasado por GET
        usuarioActivo = Usuario.objects.get(pk=request.user.id)#obtiene el usuario de session
        articulo = Articulo.objects.get(pk=id)#obtiene el articulo actual
        newBid = form.save(commit=False)#matenemos abierto el formulario para su agregacion
        newBid.articulo=articulo
        newBid.usuario=usuarioActivo
        newBid.save()
        return redirect('/articulos/detalle/' + id)

       #Se haya o no enviado el formulario volvemos a enviar para subir la puja

def comprar(request, articulo_id):
        # Optención del usuario activo
        userActive = Usuario.objects.get(pk=request.user.id) # Obtiene el el usuario usando el id obtenido desde la sesión

        # Can use standard form
        # form = UserCreationForm(request.POST)
        # Or customize it
        form = nuevaCompra()
        articulo = Articulo.objects.get(pk=articulo_id)#obtiene el articulo actual
        Comprar = form.save(commit=False)
        Comprar.usuario = userActive
        Comprar.articulo=articulo
        Comprar.save()
        articulo.fechaFin=articulo.fechaInicio

        form=NuevoArticulo(instance = articulo) #Los datos recibidos los guardamos en la variable form segun la instancia player
        actualizaArticulo = form.save(commit=False)
        actualizaArticulo.fechaFin=articulo.fechaInicio
        actualizaArticulo.save() #para guardar
        
        return redirect('/')
def listCompras(request):
    list= Compra.objects.all() #obtiene todos y los ordena por nombre
    userActive = Usuario.objects.get(pk=request.user.id)
    listPujas= Puja.objects.filter(usuario=userActive)
    context = {'comprasList' : list,'listPujas':listPujas} ## Se le anade un contexto a la lista para poder tratar los datos en el template
    return render(request, 'articulos/misCompras.html', context) ## Se devuelve la informacion al template
 
    
  