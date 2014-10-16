#encoding: utf-8

from django.forms import ModelForm
from django import forms
from usuarios.models import Usuario
from django.contrib.auth.forms import UserCreationForm
from subasta.models import Mensaje

class MyUserForm(UserCreationForm):
    """A form for creating new users. Includes all the required fields, plus a repeated password."""
    password1 = forms.CharField(label='Clave', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Clave confirmacion', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'username','fechaNacimiento' ,'email','cp','direccion','nif','avatar')#campos que deben aparecer en un formulario

    def _init_(self, *args, **kwargs):
        super(ModelForm,self).__init__(*args,**kwargs)
        self.fields['username'].label='Nombre' # Se le anade un sobrenombre a los campos de nuestro modelo
        self.fields['first_name'].label='Primer Apellido'
        self.fields['email'].label='Correo electronico'
        self.fields['fechaNacimiento'].label='Fecha de Nacimiento'
        self.fields['cp'].label='Codigo postal'
        self.fields['direccion'].label='Direccion'
        self.fields['avatar'].label = "Imagen de perfil"
        self.fields['avatar'].widget.attrs.update({'class' : 'file'})
        self.fields['avatar'].widget.attrs.update({'accept' : 'image/*'})

   

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            Usuario.objects.get(username = username)
        except Usuario.DoesNotExist:
            return username
        raise forms.ValidationError("Tu usuario ya existe")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError("Las claves no coinciden.")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user

class EditUserForm(ModelForm):
    """A form for creating new users. Includes all the required fields, plus a repeated password."""


    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'username','fechaNacimiento' ,'email','cp','direccion','nif','avatar')#campos que deben aparecer en un formulario

    def _init_(self, *args, **kwargs):
        super(ModelForm,self).__init__(*args,**kwargs)
        self.fields['username'].label='Nombre' # Se le anade un sobrenombre a los campos de nuestro modelo
        self.fields['first_name'].label='Primer Apellido'
        self.fields['email'].label='Correo electronico'
        self.fields['fechaNacimiento'].label='Fecha de Nacimiento'
        self.fields['cp'].label='Codigo postal'
        self.fields['direccion'].label='Direccion'
        self.fields['avatar'].label = "Imagen de perfil"
        self.fields['avatar'].widget.attrs.update({'class' : 'file'})
        self.fields['avatar'].widget.attrs.update({'accept' : 'image/*'})

class FormNuevoMensaje(ModelForm):
    """A form for creating new users. Includes all the required fields, plus a repeated password."""


    class Meta:
        model = Mensaje
        fields = ('usuarioReceptor', 'mensaje', 'asunto')#campos que deben aparecer en un formulario

    def _init_(self, *args, **kwargs):
        super(ModelForm,self).__init__(*args,**kwargs)
        self.fields['usuarioReceptor'].label='Destino'

