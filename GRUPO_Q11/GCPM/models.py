# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from django.db import models

class Archivo(models.Model):
    id_archivo = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=True)
    archivo = models.CharField(max_length=512)
    id_item = models.ForeignKey('Item', db_column='id_item', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'archivo'

class Atributo(models.Model):
    id_atributo = models.BigIntegerField(primary_key=True)
    tipo = models.BigIntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True)
    id_tipo_item = models.ForeignKey('TipoItem', db_column='id_tipo_item', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'atributo'

class Comite(models.Model):
    id_comite = models.BigIntegerField(primary_key=True)
    participantes = models.BigIntegerField(blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', db_column='id_usuario', blank=True, null=True)
    id_proyecto = models.ForeignKey('Proyecto', db_column='id_proyecto', unique=True, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'comite'

class Fase(models.Model):
    id_fase = models.BigIntegerField(primary_key=True)
    nro_secuencia = models.BigIntegerField(blank=True, null=True)
    estado = models.BigIntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=512, blank=True)
    class Meta:
        managed = False
        db_table = 'fase'

class Item(models.Model):
    id_item = models.BigIntegerField(primary_key=True)
    codigo = models.BigIntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    estado = models.BigIntegerField(blank=True, null=True)
    prioridad = models.BigIntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=512, blank=True)
    fehca_cracion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    padre = models.BigIntegerField(blank=True, null=True)
    antecesor = models.BigIntegerField(blank=True, null=True)
    id_tipo_item = models.ForeignKey('TipoItem', db_column='id_tipo_item', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'item'

class LineaBase(models.Model):
    id_linea_base = models.BigIntegerField(primary_key=True)
    nro_items = models.BigIntegerField()
    estado = models.BigIntegerField(blank=True, null=True)
    id_fase = models.ForeignKey(Fase, db_column='id_fase', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'linea_base'

class LineaBaseItem(models.Model):
    id_linea_base = models.ForeignKey(LineaBase, db_column='id_linea_base')
    id_item_item = models.ForeignKey(Item, db_column='id_item_item')
    class Meta:
        managed = False
        db_table = 'linea_base_item'

class Permiso(models.Model):
    id_permiso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=512, blank=True)
    class Meta:
        managed = False
        db_table = 'permiso'

class Proyecto(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=False)
    descripcion = models.CharField(max_length=512, blank=True)
    estado = models.BigIntegerField()
    fecha = models.CharField(max_length=20)
    complejidad = models.FloatField(blank=True, null=True)
    costo = models.FloatField(blank=True, null=True)
    lider = models.ForeignKey('Usuario', db_column='lider', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'proyecto'

class ProyectoFase(models.Model):
    id_proyecto_proyecto = models.ForeignKey(Proyecto, db_column='id_proyecto_proyecto')
    id_fase_fase = models.ForeignKey(Fase, db_column='id_fase_fase')
    class Meta:
        managed = False
        db_table = 'proyecto_fase'

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=512, blank=True)
    permisos = models.ManyToManyField(Permiso, through='RolPermiso')
    class Meta:
        managed = False
        db_table = 'rol'

class RolPermiso(models.Model):
    id_permiso = models.ForeignKey(Permiso, db_column='id_permiso')
    id_rol = models.ForeignKey(Rol, db_column='id_rol')
    class Meta:
        managed = False
        db_table = 'rol_permiso'

class RolUsuario(models.Model):
    id_usuario_usuario = models.ForeignKey('Usuario', db_column='id_usuario_usuario')
    id_rol_rol = models.ForeignKey(Rol, db_column='id_rol_rol')
    class Meta:
        managed = False
        db_table = 'rol_usuario'

class Solicitud(models.Model):
    id_solicitud = models.BigIntegerField(primary_key=True)
    fecha = models.DateTimeField()
    estado = models.BigIntegerField(blank=True, null=True)
    costo = models.FloatField(blank=True, null=True)
    complejidad = models.FloatField(blank=True, null=True)
    votos_favor = models.BigIntegerField(blank=True, null=True)
    votos_contra = models.BigIntegerField(blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', db_column='id_usuario', blank=True, null=True)
    id_comite = models.ForeignKey(Comite, db_column='id_comite', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'solicitud'

class SolicitudItem(models.Model):
    id_solicitud_solicitud = models.ForeignKey(Solicitud, db_column='id_solicitud_solicitud')
    id_item = models.ForeignKey(Item, db_column='id_item')
    class Meta:
        managed = False
        db_table = 'solicitud_item'

class TipoItem(models.Model):
    id_tipo_item = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=512, blank=True)
    estado = models.BigIntegerField(blank=True, null=True)
    numero = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tipo_item'

class MyUserManager(BaseUserManager):
    def create_user(self, nombre_usuario, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not nombre_usuario:
            raise ValueError('Debe especificar el nombre de usuario.')

        user = self.model(
            nombre_usuario=nombre_usuario
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre_usuario, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(nombre_usuario,
                                password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=20, blank=True)
    apellido = models.CharField(max_length=20, blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    documento = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'nombre_usuario'
    objects = MyUserManager()

    def get_full_name(self):
        return self.nombre + ' ' + self.apellido

    def get_short_name(self):
        return self.nombre

    def __str__(self):              # __unicode__ on Python 2
        return self.nombre_usuario

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        db_table = 'usuario'


class UsuarioProyecto(models.Model):
    id_usuario_usuario = models.ForeignKey(Usuario, db_column='id_usuario_usuario')
    id_proyecto_proyecto = models.ForeignKey(Proyecto, db_column='id_proyecto_proyecto')
    class Meta:
        db_table = 'usuario_proyecto'

class UsuarioRolFase(models.Model):
    id_usuario = models.ForeignKey(Usuario, db_column='id_usuario')
    id_rol = models.ForeignKey(Rol, db_column='id_rol')
    id_fase = models.ForeignKey(Fase, db_column='id_fase')
    class Meta:
        db_table = 'usuario_rol_fase'