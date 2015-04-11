from django import forms
from django.forms import ModelForm
import time
from GRUPO_Q11.GCPM import models


class CrearUsuarioForm(ModelForm):
    """
    Form de creacion de usuario
    Permite persistir los Usuarios creados con los parametros enviados desde el formulario Crear Usuario
    """
    class Meta:
        model = models.Usuario
        fields = ['nombre_usuario', 'password', 'nombre', 'apellido', 'telefono', 'documento']

    def __init__(self, *args, **kwargs):
        super(CrearUsuarioForm, self).__init__(*args, **kwargs)
        self.fields['nombre_usuario'].error_messages = {'required': 'Este campo es requerido.',
                                                        'unique': 'Usuario con este nombre ya existe.'}
        self.fields['password'].error_messages = {'required': 'Este campo es requerido.'}
        self.fields['documento'].error_messages = {'required': 'Este campo es requerido.'}


class CrearRolForm(ModelForm):
    """
    Form de creacion de Rol
    Permite persistir los Roles creados con los parametros enviados desde el formulario Crear Rol
    """
    class Meta:
        model = models.Rol
        fields = ['nombre', 'descripcion']

    def __init__(self, *args, **kwargs):
        super(CrearRolForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].error_messages = {'required': 'Este campo es requerido.',
                                                        'unique': 'Rol con este nombre ya existe.'}

class CrearProyectoForm(ModelForm):
    """
    Form de creacion de proyecto
     Permite persistir los Proyectos creados con los parametros enviados desde el formulario Crear Proyecto
    """
    class Meta:
        model = models.Proyecto
        fields = ['nombre', 'descripcion', 'estado']
    def __init__(self, *args, **kwargs):
        super(CrearProyectoForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].error_messages = {'required': 'Este campo es requerido.'}
        self.fields['descripcion'].error_messages = {'required': 'Este campo es requerido.'}

class CrearUsuarioRolForm(ModelForm):
    """
    Form de creacion de Usuario por Rol
     Permite persistir los los Roloes asigandos a un usuarios con los parametros seleccionados de la lista de roles
    """
    class Meta:
        model = models.RolUsuario
        fields = ['id_usuario_usuario', 'id_rol_rol']
    def __init__(self, *args, **kwargs):
        super(CrearUsuarioRolForm, self).__init__(*args, **kwargs)
        self.fields['id_usuario_usuario'].error_messages = {'required': 'Este campo es requerido.'}
        self.fields['id_rol_rol'].error_messages = {'required': 'Este campo es requerido.'}



class ListarForm(forms.Form):
    """
    Form de listado
    Permite desplegar listas dinamicamente deacuerdo a los parametros de las mismas.
    Se utiliza para todos los listar.
    """
    query = forms.CharField(max_length=30)