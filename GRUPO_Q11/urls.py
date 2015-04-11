from django.conf.urls import patterns, include, url
from django.contrib import admin
from GRUPO_Q11.GCPM.views import *

admin.autodiscover()

import os.path


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'GRUPO_Q11.GCPM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', logout_view),
    url(r'^adm/usuario/crear/$', crear_usuario, name='adm.usuario.crear'),
    url(r'^adm/usuario/modificar/(?P<id_usuario>\d+)/$', modificar_usuario, name='adm.usuario.modificar'),
    url(r'^adm/usuario/eliminar/(?P<id_usuario>\d+)/$', eliminar_usuario, name='adm.usuario.eliminar'),
    url(r'^adm/usuario/consultar/(?P<id_usuario>\d+)/$', consultar_usuario, name='adm.usuario.consultar'),
    url(r'^adm/usuario/listar/$', listar_usuario, name='adm.usuario.listar'),
    url(r'^adm/proyecto/crear/$', crear_proyecto, name='adm.proyecto.crear'),
    url(r'^adm/rol/crear/$', crear_rol, name='adm.rol.crear'),
    url(r'^adm/rol/consultar/(?P<id_rol>\d+)/$', consultar_rol, name='adm.rol.consultar'),
    url(r'^adm/rol/modificar/(?P<id_rol>\d+)/$', modificar_rol, name='adm.rol.modificar'),
    url(r'^adm/rol/eliminar/(?P<id_rol>\d+)/$', eliminar_rol, name='adm.rol.eliminar'),
    url(r'^adm/proyecto/listar/$', listar_proyecto, name='adm.proyecto.listar'),
    url(r'^adm/rol/listar/$', listar_rol, name='adm.rol.listar'),
    url(r'^adm/rol/permisos/(\d+)/$', asignar_permisos, name='adm.permisos.asignar'),
    url(r'^adm/rol/asignar_rol_usuario/(?P<id_usuario>\d+)/$', asignar_rol_usuario, name='adm.rol.asignar'),
    url(r'^adm/rol/listar_permisos/$', listar_permisos, name='adm.permisos.listar'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
