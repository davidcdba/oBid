#encoding: utf-8
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from forms import MyUserForm
from usuarios.forms import EditUserForm, FormNuevoMensaje
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario
from subasta.models import Mensaje

def userLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = request.POST['username']
            passwd = request.POST['password']
            access = authenticate(username=user, password=passwd)
            if access is not None:
                if access.is_active:
                    login(request, access)
                    return redirect('/')
                else:
                    return render(request, 'usuarios/nuevo.html')
            else:
                return render(request, 'usuarios/nuevo.html')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request,'usuarios/login.html', context)

@login_required(login_url='/usuarios/login')
def userLogout(request):
    logout(request)
    return redirect('/')
#funcion para crear nuevos usuario 
def usersNew(request):
    # if (request.user.is_superuser and request.user.is_staff):
    if request.method == 'POST':
        # Can use standard form
        # form = UserCreationForm(request.POST)
        # Or customize it
        form = MyUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        # form = UserCreationForm()
        form = MyUserForm()
    context = {'form':form}
    return render(request, 'usuarios/nuevo.html',  context)

def editar(request):
    UsuarioD = Usuario.objects.get(pk=request.user.id) # Obtiene el usuario usando el id obtenido desde la sesión #obtengo la informacion del usuario
    if request.method == 'POST': #en caso de que recibimos informacion del formulario
         # formulario enviado
        form=EditUserForm(request.POST, request.FILES, instance = UsuarioD) #Los datos recibidos los guardamos en la variable form segun la instancia player
        if form.is_valid():# formulario validado correctamente
            form.save() #para guardar
            return redirect('/')#redirigimos a la principal
    else:
        # formulario inicial
        form = EditUserForm(instance = UsuarioD) #prepara el formulario en la clase form con la informacion del usuario
    context={'form' : form } #se le anade el contexto form a la clase form
    return render(request,'usuarios/editarUsuario.html',context) #Se devuelve la informacion al template

def NuevoMensaje(request):
    # if (request.user.is_superuser and request.user.is_staff):
    if request.method == 'POST':
        # Can use standard form
        # form = UserCreationForm(request.POST)
        # Or customize it
        form = FormNuevoMensaje(request.POST)
        
        userActive = Usuario.objects.get(pk=request.user.id)#obtiene el usuario actual
        mensajear = form.save(commit=False)
        mensajear.usuarioEmisor = userActive #registramos la foreing key
        mensajear.save()
        return redirect('/')
    else:
        # form = UserCreationForm()
        form = FormNuevoMensaje()
    context = {'form':form}
    return render(request, 'usuarios/nuevoMensaje.html',  context)
def mensajes(request):
    
    userActive = Usuario.objects.get(pk=request.user.id)
    list= Mensaje.objects.filter(usuarioReceptor=userActive)
    context = {'mensajes' : list,} ## Se le anade un contexto a la lista para poder tratar los datos en el template
    return render(request, 'usuarios/mensajes.html', context) ## Se devuelve la informacion al template
 