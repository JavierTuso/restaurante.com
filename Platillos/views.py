from django.shortcuts import render, redirect
from .models import Provincia
from .models import Cliente
from .models import Pedido
from .models import Tipo
from .models import Platillo
from .models import Ingrediente
from .models import Receta
from .models import Detalle
from django.contrib import messages

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')



def listadoProvincia(request):
    provinciasBdd = Provincia.objects.all()
    return render(request, 'provincia.html',{'provincias': provinciasBdd})

def guardarProvincia(request):
    region_jt = request.POST["region_jt"]
    nombre_jt= request.POST["nombre_jt"]
    capital_jt= request.POST["capital_jt"]
    ciudad_jt = request.POST["ciudad_jt"]


    # Insertando datos mediante ORM de Django
    nuevoProvincia = Provincia.objects.create(
        region_jt=region_jt,
        nombre_jt=nombre_jt,
        capital_jt=capital_jt,
        ciudad_jt=ciudad_jt
    )

    messages.success(request, 'Guardado exitosamente')
    return redirect('/provincia/')


def eliminarProvincia(request, id_jt):
    provinciaEliminar = Provincia.objects.get(id_jt=id_jt)
    provinciaEliminar.delete()
    messages.error(request, 'Eliminado exitosamente')
    return redirect('/provincia/')


def editarProvincia(request, id_jt):
    provinciaEditar = Provincia.objects.get(id_jt=id_jt)
    return render(request, 'editarProvincia.html', {'provincia': provinciaEditar})


def procesarActualizacionProvincia(request, id_jt):
    id_jt = request.POST["id_jt"]
    region_jt = request.POST["region_jt"]
    nombre_jt = request.POST["nombre_jt"]
    capital_jt = request.POST["capital_jt"]
    ciudad_jt = request.POST["ciudad_jt"]


    # Insertando datos mediante ORM de Django
    provinciaEditar = Provincia.objects.get(id_jt=id_jt)
    provinciaEditar.region_jt = region_jt
    provinciaEditar.nombre_jt = nombre_jt
    provinciaEditar.capital_jt = capital_jt
    provinciaEditar.ciudad_jt = ciudad_jt

    provinciaEditar.save()

    messages.success(request, 'Actualizado Exitosamente')
    return redirect('/provincia/')
#33333333333333333333333333333333


def listadoCliente(request):
    clientesBdd = Cliente.objects.all()
    provinciasBdd = Provincia.objects.all()
    return render(request, 'Cliente.html', {'clientes': clientesBdd,'provincias':provinciasBdd})

#capturando tipos seleccionados
def guardarCliente(request):
    id_jt_nombre_jt = request.POST["provincia"]
    provinciaSeleccionado = Provincia.objects.get(id_jt=id_jt_nombre_jt)
    cedula_jt = request.POST["cedula_jt"]
    apellido_jt = request.POST["apellido_jt"]
    nombre_jt = request.POST["nombre_jt"]
    direccion_jt = request.POST["direccion_jt"]
    fecha_nacimiento_jt = request.POST["fecha_nacimiento_jt"]
    correo_jt = request.POST["correo_jt"]


    # Insertando datos mediante ORM de Django
    nuevoCliente = Cliente.objects.create(
        cedula_jt=cedula_jt,
        apellido_jt=apellido_jt,
        nombre_jt=nombre_jt,
        direccion_jt=direccion_jt,
        fecha_nacimiento_jt=fecha_nacimiento_jt,
        correo_jt=correo_jt,
        provincia=provinciaSeleccionado

    )

    messages.success(request, 'Cliente guardado exitosamente')
    return redirect('/cliente/')


def eliminarCliente(request, id_jt):
    clienteEliminar = Cliente.objects.get(id_jt=id_jt)
    clienteEliminar.delete()
    messages.error(request, 'Cliente eliminado exitosamente')
    return redirect('/cliente/')


def editarCliente(request, id_jt):
    clienteEditar = Cliente.objects.get(id_jt=id_jt)
    provinciasBdd = Provincia.objects.all()
    return render(request, 'editarCliente.html', {'cliente': clienteEditar,'provincias':provinciasBdd})


def procesarActualizacionCliente(request, id_jt):
    id_jt = request.POST["id_jt"]
    id_jt_nombre_jt = request.POST["provincia"]
    provinciaSeleccionado = Provincia.objects.get(id_jt=id_jt_nombre_jt)
    cedula_jt = request.POST["cedula_jt"]
    apellido_jt = request.POST["apellido_jt"]
    nombre_jt = request.POST["nombre_jt"]
    direccion_jt = request.POST["direccion_jt"]
    fecha_nacimiento_jt = request.POST["fecha_nacimiento_jt"]
    correo_jt = request.POST["correo_jt"]


    # Insertando datos mediante ORM de Django
    clienteEditar = Cliente.objects.get(id_jt=id_jt)
    clienteEditar.cedula_jt = cedula_jt
    clienteEditar.apellido_jt = apellido_jt
    clienteEditar.nombre_jt = nombre_jt
    clienteEditar.provincia=provinciaSeleccionado
    clienteEditar.direccion_jt = direccion_jt
    clienteEditar.fecha_nacimiento_jt = fecha_nacimiento_jt
    clienteEditar.correo_jt = correo_jt
    clienteEditar.save()

    messages.success(request, 'Cliente ACTUALIZADO Exitosamente')
    return redirect('/cliente/')

#33333333333333333333333333333333
def listadoTipo(request):
    tiposBdd = Tipo.objects.all()
    return render(request, 'tipo.html',{'tipos': tiposBdd})

def guardarTipo(request):
    nombreTipo_jt = request.POST["nombreTipo_jt"]
    descripcionTipo_jt= request.POST["descripcionTipo_jt"]
    categoriaTipo_jt= request.POST["categoriaTipo_jt"]


    # Insertando datos mediante ORM de Django
    nuevoTipo = Tipo.objects.create(
        nombreTipo_jt=nombreTipo_jt,
        descripcionTipo_jt=descripcionTipo_jt,
        categoriaTipo_jt=categoriaTipo_jt,
    )

    messages.success(request, 'Guardado exitosamente')
    return redirect('/tipo/')


def eliminarTipo(request, idTipo_jt):
    tipoEliminar = Tipo.objects.get(idTipo_jt=idTipo_jt)
    tipoEliminar.delete()
    messages.error(request, 'Eliminado exitosamente')
    return redirect('/tipo/')


def editarTipo(request, idTipo_jt):
    tipoEditar = Tipo.objects.get(idTipo_jt=idTipo_jt)
    return render(request, 'editarTipo.html', {'tipo': tipoEditar})


def procesarActualizacionTipo(request, idTipo_jt):
    idTipo_jt = request.POST["idTipo_jt"]
    nombreTipo_jt = request.POST["nombreTipo_jt"]
    descripcionTipo_jt = request.POST["descripcionTipo_jt"]
    categoriaTipo_jt = request.POST["categoriaTipo_jt"]


    # Insertando datos mediante ORM de Django
    tipoEditar = Tipo.objects.get(idTipo_jt=idTipo_jt)
    tipoEditar.nombreTipo_jt = nombreTipo_jt
    tipoEditar.descripcionTipo_jt = descripcionTipo_jt
    tipoEditar.categoriaTipo_jt = categoriaTipo_jt
    tipoEditar.save()

    messages.success(request, 'Actualizado Exitosamente')
    return redirect('/tipo/')
#$4444444444444444444444444444444444444


def listadoPlatillo(request):
    platillosBdd = Platillo.objects.all()
    tiposBdd = Tipo.objects.all()
    return render(request, 'platillo.html', {'platillos': platillosBdd, 'tipos': tiposBdd})

#capturando tipos seleccionados
def guardarPlatillo(request):
    idTipo_jt_nombreTipo_jt = request.POST["tipo"]
    nombrePlatillo_jt = request.POST["nombrePlatillo_jt"]
    tipoSeleccionado = Tipo.objects.get(idTipo_jt=idTipo_jt_nombreTipo_jt)
    descripcionPlatillo_jt = request.POST["descripcionPlatillo_jt"]
    precioPlatillo_jt = request.POST["precioPlatillo_jt"]



    # Insertando datos mediante ORM de Django
    nuevoPlatillo = Platillo.objects.create(
        nombrePlatillo_jt=nombrePlatillo_jt,
        tipo=tipoSeleccionado,
        descripcionPlatillo_jt=descripcionPlatillo_jt,
        precioPlatillo_jt=precioPlatillo_jt,

    )

    messages.success(request, 'Guardado exitosamente')
    return redirect('/platillo/')


def eliminarPlatillo(request, idPlatillo_jt):
    platilloEliminar = Platillo.objects.get(idPlatillo_jt=idPlatillo_jt)
    platilloEliminar.delete()
    messages.error(request, 'Eliminado exitosamente')
    return redirect('/platillo/')


def editarPlatillo(request, idPlatillo_jt):
    platilloEditar = Platillo.objects.get(idPlatillo_jt=idPlatillo_jt)
    tiposBdd = Tipo.objects.all()
    return render(request, 'editarPlatillo.html', {'platillo': platilloEditar, 'tipos': tiposBdd})


def procesarActualizacionPlatillo(request, idPlatillo_jt):
    idPlatillo_jt = request.POST["idPlatillo_jt"]
    idTipo_jt_nombreTipo_jt = request.POST["tipo"]
    tipoSeleccionado = Tipo.objects.get(idTipo_jt=idTipo_jt_nombreTipo_jt)
    nombrePlatillo_jt = request.POST["nombrePlatillo_jt"]
    descripcionPlatillo_jt = request.POST["descripcionPlatillo_jt"]
    precioPlatillo_jt = request.POST["precioPlatillo_jt"]

    platilloEditar = Platillo.objects.get(idPlatillo_jt=idPlatillo_jt)
    platilloEditar.nombrePlatillo_jt = nombrePlatillo_jt
    platilloEditar.descripcionPlatillo_jt = descripcionPlatillo_jt
    platilloEditar.tipo = tipoSeleccionado
    platilloEditar.precioPlatillo_jt = precioPlatillo_jt
    platilloEditar.save()

    messages.success(request, 'ACTUALIZADO Exitosamente')
    return redirect('/platillo/')
#33333333333333333333333333333333333333333333


def listadoPedido(request):
    pedidosBdd = Pedido.objects.all()
    clientesBdd = Cliente.objects.all()
    tiposBdd = Tipo.objects.all()
    platillosBdd = Platillo.objects.all()
    return render(request, 'pedido.html', {'pedidos': pedidosBdd,'clientes':clientesBdd,'tipos': tiposBdd,'platillos': platillosBdd})

#capturando tipos seleccionados
def guardarPedido(request):
    id_jt_nombre_jt = request.POST["nombre"]
    nombreSeleccionado = Cliente.objects.get(id_jt=id_jt_nombre_jt)
    idTipo_jt_nombreTipo_jt = request.POST["tipo"]
    tipoSeleccionado = Tipo.objects.get(idTipo_jt=idTipo_jt_nombreTipo_jt)
    idPlatillo_jt_nombrePlatillo_jt = request.POST["platillo"]
    platilloSeleccionado = Platillo.objects.get(idPlatillo_jt=idPlatillo_jt_nombrePlatillo_jt)
    fechaPedido_jt = request.POST["fechaPedido_jt"]
    descripcionPedido_jt = request.POST["descripcionPedido_jt"]
    horaPedido_jt = request.POST["horaPedido_jt"]
    fotografiaPedido_jt=request.FILES.get("fotografiaPedido_jt")



    # Insertando datos mediante ORM de Django
    nuevoPedido = Pedido.objects.create(
        fechaPedido_jt=fechaPedido_jt,
        descripcionPedido_jt=descripcionPedido_jt,
        horaPedido_jt=horaPedido_jt,
        fotografiaPedido_jt=fotografiaPedido_jt,
        nombre=nombreSeleccionado,
        tipo=tipoSeleccionado,
        platillo=platilloSeleccionado,


    )

    messages.success(request, 'Guardado exitosamente')
    return redirect('/pedido/')


def eliminarPedido(request, idPedido_jt):
    pedidoEliminar = Pedido.objects.get(idPedido_jt=idPedido_jt)
    pedidoEliminar.delete()
    messages.error(request, 'Eliminado exitosamente')
    return redirect('/pedido/')


def editarPedido(request, idPedido_jt):
    pedidoEditar = Pedido.objects.get(idPedido_jt=idPedido_jt)
    clientesBdd = Cliente.objects.all()
    tiposBdd = Tipo.objects.all()
    platillosBdd = Platillo.objects.all()
    return render(request, 'editarPedido.html', {'pedido': pedidoEditar,'clientes':clientesBdd, 'tipos': tiposBdd, 'platillos': platillosBdd})


def procesarActualizacionPedido(request, idPedido_jt):
    idPedido_jt = request.POST["idPedido_jt"]
    id_jt_nombre_jt = request.POST["nombre"]
    nombreSeleccionado = Cliente.objects.get(id_jt=id_jt_nombre_jt)
    idTipo_jt_nombreTipo_jt = request.POST["tipo"]
    tipoSeleccionado = Tipo.objects.get(idTipo_jt=idTipo_jt_nombreTipo_jt)
    idPlatillo_jt_nombrePlatillo_jt = request.POST["platillo"]
    platilloSeleccionado = Platillo.objects.get(idPlatillo_jt=idPlatillo_jt_nombrePlatillo_jt)
    fechaPedido_jt = request.POST["fechaPedido_jt"]
    descripcionPedido_jt = request.POST["descripcionPedido_jt"]
    horaPedido_jt = request.POST["horaPedido_jt"]
    fotografiaPedido_jt=request.FILES.get("fotografiaPedido_jt")




    # Insertando datos mediante ORM de Django
    pedidoEditar = Pedido.objects.get(idPedido_jt=idPedido_jt)
    pedidoEditar.fechaPedido_jt = fechaPedido_jt
    pedidoEditar.descripcionPedido_jt = descripcionPedido_jt
    pedidoEditar.nombre=nombreSeleccionado
    pedidoEditar.tipo=tipoSeleccionado
    pedidoEditar.platillo=platilloSeleccionado
    pedidoEditar.horaPedido_jt = horaPedido_jt
    pedidoEditar.fotografiaPedido_jt = fotografiaPedido_jt
    pedidoEditar.save()

    messages.success(request, 'ACTUALIZADO Exitosamente')
    return redirect('/pedido/')
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def listadoIngrediente(request):
    ingredientesBdd = Ingrediente.objects.all()
    return render(request, 'ingrediente.html',{'ingredientes': ingredientesBdd})

def guardarIngrediente(request):
    nombreIngrediente_jt = request.POST["nombreIngrediente_jt"]
    fechaExpiracion_jt= request.POST["fechaExpiracion_jt"]
    fotografiaIngrediente_jt=request.FILES.get("fotografiaIngrediente_jt")


    # Insertando datos mediante ORM de Django
    nuevoIngrediente = Ingrediente.objects.create(
        nombreIngrediente_jt=nombreIngrediente_jt,
        fechaExpiracion_jt=fechaExpiracion_jt,
        fotografiaIngrediente_jt=fotografiaIngrediente_jt,
    )

    messages.success(request, 'Guardado exitosamente')
    return redirect('/ingrediente/')


def eliminarIngrediente(request, idIngrediente_jt):
    ingredienteEliminar = Ingrediente.objects.get(idIngrediente_jt=idIngrediente_jt)
    ingredienteEliminar.delete()
    messages.error(request, 'Eliminado exitosamente')
    return redirect('/ingrediente/')


def editarIngrediente(request, idIngrediente_jt):
    ingredienteEditar = Ingrediente.objects.get(idIngrediente_jt=idIngrediente_jt)
    return render(request, 'editarIngrediente.html', {'ingrediente': ingredienteEditar})


def procesarActualizacionIngrediente(request, idIngrediente_jt):
    nombreIngrediente_jt = request.POST["nombreIngrediente_jt"]
    fechaExpiracion_jt = request.POST["fechaExpiracion_jt"]
    fotografiaIngrediente_jt=request.FILES.get("fotografiaIngrediente_jt")


    # Insertando datos mediante ORM de Django
    ingredienteEditar = Ingrediente.objects.get(idIngrediente_jt=idIngrediente_jt)
    ingredienteEditar.nombreIngrediente_jt = nombreIngrediente_jt
    ingredienteEditar.fechaExpiracion_jt = fechaExpiracion_jt
    ingredienteEditar.fotografiaIngrediente_jt = fotografiaIngrediente_jt
    ingredienteEditar.save()

    messages.success(request, 'Actualizado Exitosamente')
    return redirect('/ingrediente/')
#4444444444444444444444444444444444444

def listadoReceta(request):
    recetasBdd = Receta.objects.all()
    ingredientesBdd = Ingrediente.objects.all()
    platillosBdd = Platillo.objects.all()
    return render(request, 'receta.html', {'recetas': recetasBdd,'ingredientes': ingredientesBdd,'platillos': platillosBdd})

#capturando tipos seleccionados
def guardarReceta(request):
    idIngrediente_jt_nombreIngrediente_jt = request.POST["ingrediente"]
    ingredienteSeleccionado = Ingrediente.objects.get(idIngrediente_jt=idIngrediente_jt_nombreIngrediente_jt)
    idPlatillo_jt_nombrePlatillo_jt = request.POST["platillo"]
    platilloSeleccionado = Platillo.objects.get(idPlatillo_jt=idPlatillo_jt_nombrePlatillo_jt)
    pasosReceta_jt = request.POST["pasosReceta_jt"]
    tiempoPreparacion_jt = request.POST["tiempoPreparacion_jt"]
    dificultadReceta_jt = request.POST["dificultadReceta_jt"]



    # Insertando datos mediante ORM de Django
    nuevoReceta = Receta.objects.create(
        pasosReceta_jt=pasosReceta_jt,
        tiempoPreparacion_jt=tiempoPreparacion_jt,
        dificultadReceta_jt=dificultadReceta_jt,
        ingrediente=ingredienteSeleccionado,
        platillo=platilloSeleccionado


    )

    messages.success(request, 'Guardado exitosamente')
    return redirect('/receta/')


def eliminarReceta(request, idReceta_jt):
    recetaEliminar = Receta.objects.get(idReceta_jt=idReceta_jt)
    recetaEliminar.delete()
    messages.error(request, 'Eliminado exitosamente')
    return redirect('/receta/')


def editarReceta(request, idReceta_jt):
    recetaEditar = Receta.objects.get(idReceta_jt=idReceta_jt)
    ingredientesBdd = Ingrediente.objects.all()
    platillosBdd = Platillo.objects.all()
    return render(request, 'editarReceta.html', {'receta': recetaEditar,'ingredientes':ingredientesBdd, 'platillos': platillosBdd})


def procesarActualizacionReceta(request, idReceta_jt):
    idReceta_jt = request.POST["idReceta_jt"]
    idIngrediente_jt_nombreIngrediente_jt = request.POST["ingrediente"]
    ingredienteSeleccionado = Ingrediente.objects.get(idIngrediente_jt=idIngrediente_jt_nombreIngrediente_jt)
    idPlatillo_jt_nombrePlatillo_jt = request.POST["platillo"]
    platilloSeleccionado = Platillo.objects.get(idPlatillo_jt=idPlatillo_jt_nombrePlatillo_jt)
    pasosReceta_jt = request.POST["pasosReceta_jt"]
    tiempoPreparacion_jt = request.POST["tiempoPreparacion_jt"]
    dificultadReceta_jt = request.POST["dificultadReceta_jt"]




    # Insertando datos mediante ORM de Django
    recetaEditar = Receta.objects.get(idReceta_jt=idReceta_jt)
    recetaEditar.pasosReceta_jt = pasosReceta_jt
    recetaEditar.tiempoPreparacion_jt = tiempoPreparacion_jt
    recetaEditar.ingrediente=ingredienteSeleccionado
    recetaEditar.platillo=platilloSeleccionado
    recetaEditar.dificultadReceta_jt = dificultadReceta_jt
    recetaEditar.save()

    messages.success(request, 'ACTUALIZADO Exitosamente')
    return redirect('/receta/')
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$}

def detalle_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'detalle_pedidos.html', {'pedidos': pedidos})
