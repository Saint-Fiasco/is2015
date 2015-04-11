import datetime
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms import Form
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
import time
import GRUPO_Q11
from GRUPO_Q11.GCPM.forms import CrearUsuarioForm, ListarForm, CrearProyectoForm, CrearRolForm, CrearUsuarioRolForm
from GRUPO_Q11.GCPM.models import Usuario, Proyecto, Rol, Permiso

@login_required
def logout_view(request):
    logout(request)
    return redirect(home)


@login_required
def home(request):
    """
    Menu principal de de la aplicacion en el cual se accede desde el loguin
    """
    return render_to_response('home.html', context_instance=RequestContext(request))

@login_required
def eliminar_usuario(request, id_usuario):
    """
    eliminar un usuario
    :param request: http request
    :param id_usuario: id del usuario a eliminar
    la eliminacion es logica
    """
    usuario = Usuario.objects.get(id_usuario=id_usuario)
    if usuario is not None:
        usuario.is_active = not usuario.is_active
        usuario.save()
    return redirect('/adm/usuario/listar')



@login_required
def eliminar_rol(request, id_rol):
    """
    eliminar un rol
    :param request: http request
    :param id_rol: id del rol a eliminar
    la eliminacion es logica
    """
    rol = Rol.objects.get(id_rol=id_rol)
    print rol.is_active
    if rol is not None:
        rol.is_active = False
        rol.save()
    return redirect('/adm/rol/listar')



@login_required
def modificar_usuario(request, id_usuario):
    """
    Modificar un usuario
    :param request: http request
    :param id_usuario: id del usuario a modificar
    """
    modificar = True

    usuario = Usuario.objects.get(id_usuario=id_usuario)
    if request.method == 'POST':
        data = request.POST
        usuario.nombre = data['nombre']
        usuario.apellido = data['apellido']
        if data['password']:
            usuario.set_password(data['password'])
        usuario.telefono = data['telefono']
        usuario.documento = data['documento']
        usuario.save()
        return redirect('/adm/usuario/listar')
    else:
        if usuario:
            form = CrearUsuarioForm(instance=usuario)
        else:
            return redirect('/adm/usuario/listar')

        return render_to_response('GCPM/Usuarios/crearUsuario.html',
                                  context_instance=RequestContext(request, {"form": form, "modificar":modificar}))


@login_required
def modificar_rol(request, id_rol):
    """
    Modificar un usuario
    :param request: http request
    :param id_usuario: id del usuario a modificar
    """
    modificar = True

    rol = Rol.objects.get(id_rol=id_rol)
    if request.method == 'POST':
        data = request.POST
        # rol.nombre = data['nombre']
        rol.descripcion = data['descripcion']
        rol.save()
        return redirect('/adm/rol/listar')
    else:
        if rol:
            form = CrearRolForm(instance=rol)
        else:
            redirect('/adm/rol/listar')

    return render_to_response('GCPM/Rol/crearRol.html',
                                  context_instance=RequestContext(request, {"form": form, "modificar":modificar}))

@login_required
def consultar_usuario(request, id_usuario):
    """
    Consultar un usuario
    :param request: http request
    :param id_usuario: id del usuario a Consultar
    """
    consultar = True

    usuario = Usuario.objects.get(id_usuario=id_usuario)
    if usuario:
        form = CrearUsuarioForm(instance=usuario)
    else:
        return redirect('/adm/usuario/listar')

    return render_to_response('GCPM/Usuarios/crearUsuario.html',
                              context_instance=RequestContext(request, {"form": form, "consultar":consultar}))

@login_required
def consultar_rol(request, id_rol):
    """
    Consultar un usuario
    :param request: http request
    :param id_usuario: id del usuario a Consultar
    """
    consultar = True

    rol = Rol.objects.get(id_rol=id_rol)
    if rol:
        form = CrearRolForm(instance=rol)
    else:
        return redirect('/adm/rol/listar')

    return render_to_response('GCPM/Rol/crearRol.html',
                              context_instance=RequestContext(request, {"form": form, "consultar":consultar}))

@login_required
def crear_usuario(request):
    """
    Vista del formulario de creacion de usuarios 'forms.py'
    :param request: http request
    Permite crear usuarios por medio de un formulario con siguientes campos
    +Nombre Usuario
    +Password
    +Nombre
    +Apellido
    +Telefono
    +Documento
    """
    mensaje = ''
    if request.method == 'POST':
        form = CrearUsuarioForm(data=request.POST)

        if form.is_valid():
            usuario = form.save()
            usuario.set_password(usuario.password)
            usuario.save()
            request.session['success'] = 'Creado.'
            return redirect(listar_usuario)

    else:
        form = CrearUsuarioForm()
    return render_to_response('GCPM/Usuarios/crearUsuario.html',
                              context_instance=RequestContext(request, {"form": form, "mensaje": mensaje}))


@login_required
def crear_rol(request):
    """
    Vista del formulario de creacion de roles. Ver forms.py
    :param request: http request
    Permite crear Roles a partir de un formulario con los siguientes campos
    +Nombre
    +Descripcion
    """
    mensaje = ''
    if request.method == 'POST':
        form = CrearRolForm(data=request.POST)

        if form.is_valid():
            rol = form.save()
            #rol.set_password(usuario.password)
            rol.save()
            mensaje = 'Creado.'

    else:
        form = CrearRolForm()
    return render_to_response('GCPM/Rol/crearRol.html',
                              context_instance=RequestContext(request, {"form": form, "mensaje": mensaje}))

@login_required
def crear_proyecto(request):
    """
    Vista del formulario de creacion de proyectos 'forms.py'
    :param request: http request
    Permite crer proyectos a travez de un frmulario con los sigueintes campos
    +Nombree
    +Descripcion
    Setea los demas valor requeridos por el proyecto por default
    """
    mensaje = ''
    if request.method == 'POST':
        form = CrearProyectoForm(data=request.POST)

        if form.is_valid():
            proyecto = form.save()
            proyecto.lider = request.user
            proyecto.complejidad = 0.0
            proyecto.fecha = str(datetime.date.today())
            proyecto.costo = 0
            proyecto.save()
            mensaje = 'Creado.'

    else:
        form = CrearProyectoForm()
    return render_to_response('GCPM/Proyectos/crearProyecto.html',
                              RequestContext(request, {"form": form, "mensaje":mensaje}))

@login_required
def usuarioRol(request):
    """

    """
    mensaje = ''
    if request.method == 'POST':
        form = CrearUsuarioRolForm(data=request.POST)

        if form.is_valid():
            rolesUsuario = form.save()
            rolesUsuario.id_rol_rol = request.user
            rolesUsuario.id_usuario_usuario = 0.0
            mensaje = 'Creado.'

    else:
        form = CrearUsuarioRolForm()
    return render_to_response('GCPM/Usuarios/listarUsuario.html',
                              RequestContext(request, {"form": form, "mensaje":mensaje}))

@login_required
def listar_usuario(request):
    """
    Lista de usuarios
    :param request: http request
    Despliega los usuarios y sus datos:
    +Nombre Usuario
    +Nombre
    +Apellido
    +Documento
    +Telefono
    """
    if request.session.has_key('success'):
        mensaje = request.session['success']
        request.session['success'] = None
    else:
        mensaje = None
    print mensaje
    query = ''
    sort = None
    activo = None
    page = 1
    Usuarios = None
    queryform = ListarForm()

    # En caso que sea POST se hizo una busqueda
    if request.method == 'POST':
        queryform = ListarForm(data=request.POST)

        sort = request.POST.get('sort')
        activo = request.POST.get('activos')
        if queryform.is_valid():
            query = queryform.cleaned_data.get('query')


        # request.session['prevSearch'] = Proyectos
        request.session['query'] = query
        request.session['sort'] = sort
        request.session['activo'] = activo
    # Si es un GET se obtiene la pagina. Puede que no se haya realizado ninguna busqueda.
    else:
        page = request.GET.get('page')
        if page is None:
            request.session['query'] = ''
            request.session['sort'] = None
            request.session['activo'] = None
            query = ''
        else:
            if request.session.has_key('query'):
                query = request.session['query']
            if request.session.has_key('sort'):
                sort = request.session['sort']
            if request.session.has_key('activo'):
                activo = request.session['activo']
    if query is None:
        query = ''
    byUsuario = Usuario.objects.filter(nombre_usuario__icontains=query)
    byNombre = Usuario.objects.filter(nombre__icontains=query)
    byApellido = Usuario.objects.filter(apellido__icontains=query)
    byDocumento = Usuario.objects.filter(documento__icontains=query)
    Usuarios = byApellido | byNombre | byUsuario | byDocumento
    if activo == 'on':
        print activo
        Usuarios = Usuarios.filter(is_active=True)
    if sort is None:
        Usuarios = Usuarios.order_by('nombre_usuario')
    else:
        Usuarios = Usuarios.order_by(sort)
    paginator = Paginator(Usuarios, 10)
    try:
        usuarios = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        usuarios = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        usuarios = paginator.page(paginator.num_pages)

    return render_to_response('GCPM/Usuarios/listarUsuario.html',
                              RequestContext(request, {"usuarios": usuarios, "queryform": queryform, "query": query, "mensaje":mensaje}))

@login_required
def listar_proyecto(request):
    """
    Lista de proyecto
    :param request: http request
    Despliega lso proyecctos con sus atributos
    +Nombre
    +Descripcion
    +Feha Creacion
    +Costo
    +Lider
    +Estado
    """
    query = ''
    sort = None
    page = 1
    Proyectos = None
    queryform = ListarForm()
    # En caso que sea POST se hizo una busqueda
    if request.method == 'POST':
        queryform = ListarForm(data=request.POST)

        sort = request.POST.get('sort')
        if queryform.is_valid():
            query = queryform.cleaned_data.get('query')


        # request.session['prevSearch'] = Proyectos
        request.session['query'] = query
        request.session['sort'] = sort
    # Si es un GET se obtiene la pagina. Puede que no se haya realizado ninguna busqueda.
    else:
        page = request.GET.get('page')
        if page is None:
            request.session['query'] = ''
            request.session['sort'] = None
            query = ''
        else:
            if request.session.has_key('query'):
                query = request.session['query']
            if request.session.has_key('sort'):
                sort = request.session['sort']
    if query is None:
        query = ''
    byNombre = Proyecto.objects.filter(nombre__icontains=query)
    byDescripcion = Proyecto.objects.filter(descripcion__icontains=query)
    Proyectos = byNombre | byDescripcion
    if sort is not None:
        Proyectos = Proyectos.order_by(sort)
    paginator = Paginator(Proyectos, 15)
    try:
        proyectos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        proyectos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        proyectos = paginator.page(paginator.num_pages)


    return render_to_response('GCPM/Proyectos/listarProyecto.html',
                              RequestContext(request,{"proyectos":proyectos, "queryform":queryform, "query":query}))

@login_required
def listar_rol(request):
    """
    Lista de roles
    :param request:
    Despliega los roles y sus atributos:
    +Nombre
    +Descripcion
    """
    query = ''
    sort = None
    page = 1
    Roles = None
    queryform = ListarForm()
    # En caso que sea POST se hizo una busqueda
    if request.method == 'POST':
        queryform = ListarForm(data=request.POST)

        sort = request.POST.get('sort')
        if queryform.is_valid():
            query = queryform.cleaned_data.get('query')


        # request.session['prevSearch'] = Proyectos
        request.session['query'] = query
        request.session['sort'] = sort
    # Si es un GET se obtiene la pagina. Puede que no se haya realizado ninguna busqueda.
    else:
        page = request.GET.get('page')
        if page is None:
            request.session['query'] = ''
            request.session['sort'] = None
            query = ''
        else:
            if request.session.has_key('query'):
                query = request.session['query']
            if request.session.has_key('sort'):
                sort = request.session['sort']
    if query is None:
        query = ''
    byNombre = GRUPO_Q11.GCPM.models.Rol.objects.filter(nombre__icontains=query)
    byDescripcion = GRUPO_Q11.GCPM.models.Rol.objects.filter(descripcion__icontains=query)
    Rol = byNombre | byDescripcion
    if sort is not None:
        Rol = Rol.order_by(sort)
    paginator = Paginator(Rol, 15)
    try:
        roles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        roles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        roles = paginator.page(paginator.num_pages)


    return render_to_response('GCPM/Roles/listarRoles.html',
                              RequestContext(request,{"roles":roles, "queryform":queryform, "query":query}))

@login_required
def asignar_permisos(request, id_rol):
    """
    Asignar permisos a un rol.
    :param id_rol: rol a asignar
    :param request: http request
    Se recibe el id del rol como parametro.
    """
    query = ''
    queryform = ListarForm()
    sort = None
    page = 1
    rol = GRUPO_Q11.GCPM.models.Rol.objects.get(id_rol=id_rol)
    permisos_activos = rol.permisos.all()
    permiso = GRUPO_Q11.GCPM.models.Permiso.objects.all()
    paginator = Paginator(permiso, 15)
    permisos = paginator.page(1)
    return render_to_response('GCPM/Rol/Permisos.html',
                              RequestContext(request,{"permisos":permisos, "queryform":queryform, "query":query, "permisos_activos":permisos_activos, "rol":rol}))


@login_required
def asignar_rol_usuario(request, id_usuario):
    """
    Asignar Roles a un Usuario
    :param id_usuario: usuario a asignar
    :param request: http request
    ASigna multiples roles a un usuario mediante la sellecion de los mismos por medio de una lista de roles
    """
    if id_usuario is None:
        habilitar = False
    else:
        habilitar = True
    query = ''
    sort = None
    page = 1
    queryform = ListarForm()
    # En caso que sea POST se hizo una busqueda
    if request.method == 'POST':
        queryform = ListarForm(data=request.POST)

        sort = request.POST.get('sort')
        if queryform.is_valid():
            query = queryform.cleaned_data.get('query')


        # request.session['prevSearch'] = Proyectos
        request.session['query'] = query
        request.session['sort'] = sort
    # Si es un GET se obtiene la pagina. Puede que no se haya realizado ninguna busqueda.
    else:
        page = request.GET.get('page')
        if page is None:
            request.session['query'] = ''
            request.session['sort'] = None
            query = ''
        else:
            if request.session.has_key('query'):
                query = request.session['query']
            if request.session.has_key('sort'):
                sort = request.session['sort']
    if query is None:
        query = ''
    usuario = Usuario.objects.get(id_usuario=id_usuario)
    byNombre = GRUPO_Q11.GCPM.models.Rol.objects.filter(nombre__icontains=query)
    byDescripcion = GRUPO_Q11.GCPM.models.Rol.objects.filter(descripcion__icontains=query)
    Rol = byNombre | byDescripcion
    if sort is not None:
        Rol = Rol.order_by(sort)
    paginator = Paginator(Rol, 15)
    try:
        roles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        roles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        roles = paginator.page(paginator.num_pages)


    return render_to_response('GCPM/Roles/listarRoles.html',
                              RequestContext(request,{"roles":roles, "queryform":queryform, "query":query, "habilitar":habilitar, "id_usuario": id_usuario, "usuario": usuario}))

@login_required
def listar_permisos(request):
    """
    Lista de permisos
    :param request: http request
    Despliega los permisos y sus atributos
    +Nombre
    +Descripcion
    """
    query = ''
    sort = None
    page = 1
    Permisos = None
    queryform = ListarForm()
    # En caso que sea POST se hizo una busqueda
    if request.method == 'POST':
        queryform = ListarForm(data=request.POST)

        sort = request.POST.get('sort')
        if queryform.is_valid():
            query = queryform.cleaned_data.get('query')


        # request.session['prevSearch'] = Proyectos
        request.session['query'] = query
        request.session['sort'] = sort
    # Si es un GET se obtiene la pagina. Puede que no se haya realizado ninguna busqueda.
    else:
        page = request.GET.get('page')
        if page is None:
            request.session['query'] = ''
            request.session['sort'] = None
            query = ''
        else:
            if request.session.has_key('query'):
                query = request.session['query']
            if request.session.has_key('sort'):
                sort = request.session['sort']
    if query is None:
        query = ''
    byNombre = GRUPO_Q11.GCPM.models.Permiso.objects.filter(nombre__icontains=query)
    byDescripcion = GRUPO_Q11.GCPM.models.Permiso.objects.filter(descripcion__icontains=query)
    Permiso = byNombre | byDescripcion
    if sort is not None:
        Permiso = Permiso.order_by(sort)
    paginator = Paginator(Permiso, 15)
    try:
        permisos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        permisos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        permisos = paginator.page(paginator.num_pages)


    return render_to_response('GCPM/Roles/listarPermisos.html',
                              RequestContext(request,{"permisos":permisos, "queryform":queryform, "query":query}))