from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def provincia(request):
    provincias=Provincia.objects.all()
    return render(request,'provincia.html',{'provincias':provincias, 'navbar': 'provincia'})

def guardarProvincia(request):
    nombre_vj=request.POST["nombre_vj"]
    region_vj=request.POST["region_vj"]
    capital_vj=request.POST["capital_vj"]
    descripcion_vj=request.POST["descripcion_vj"]


    nuevoProvincia=Provincia.objects.create(nombre_vj=nombre_vj, region_vj=region_vj, capital_vj=capital_vj,
                                          descripcion_vj=descripcion_vj)


    return redirect('/')

def eliminarProvincia(request,id_pro_vj):
    provinciaEliminar=Provincia.objects.get(id_pro_vj=id_pro_vj)
    provinciaEliminar.delete()
    messages.success(request, 'Provincia eliminado exitosamente')
    return redirect('/')

def editarProvincia(request, id_pro_vj):
    provinciaEditar=Provincia.objects.get(id_pro_vj=id_pro_vj)
    return render(request, 'editarProvincia.html', {'provincia': provinciaEditar})

def procesarinformacionProvincia(request):
    id_pro_vj=request.POST["id_pro_vj"]
    nombre_vj=request.POST["nombre_vj"]
    region_vj=request.POST["region_vj"]
    capital_vj=request.POST["capital_vj"]
    descripcion_vj=request.POST["descripcion_vj"]
    #Insertando datos mediante el ORM de DJANGO
    provinciaEditar=Provincia.objects.get(id_pro_vj=id_pro_vj)
    provinciaEditar.nombre_vj=nombre_vj
    provinciaEditar.region_vj=region_vj
    provinciaEditar.capital_vj=capital_vj
    provinciaEditar.descripcion_vj=descripcion_vj
    provinciaEditar.save()
    messages.success(request,
      'Provincia ACTUALIZADO Exitosamente')
    return redirect('/')

def ingrediente(request):
    ingredientes=Ingrediente.objects.all()
    return render(request,'ingrediente.html',{'ingredientes':ingredientes, 'navbar': 'ingrediente'})

def guardarIngrediente(request):
    nombre_vj=request.POST["nombre_vj"]
    categoria_vj=request.POST["categoria_vj"]
    fechacadu_vj=request.POST["fechacadu_vj"]
    precio_vj=request.POST["precio_vj"]
    imagen_in_vj=request.FILES.get("imagen_in_vj")


    nuevoIngrediente=Ingrediente.objects.create(nombre_vj=nombre_vj, categoria_vj=categoria_vj, fechacadu_vj=fechacadu_vj,
                                          precio_vj=precio_vj, imagen_in_vj=imagen_in_vj)


    return redirect('/ingrediente')

def eliminarIngrediente(request,id_in_vj):
    ingredienteEliminar=Ingrediente.objects.get(id_in_vj=id_in_vj)
    ingredienteEliminar.delete()
    messages.success(request, 'Ingrediente eliminado exitosamente')
    return redirect('/ingrediente')

def editarIngrediente(request, id_in_vj):
    ingredienteEditar=Ingrediente.objects.get(id_in_vj=id_in_vj)
    return render(request, 'editarIngrediente.html', {'ingrediente': ingredienteEditar})

def procesarinformacionIngrediente(request):
    id_in_vj=request.POST["id_in_vj"]
    nombre_vj=request.POST["nombre_vj"]
    categoria_vj=request.POST["categoria_vj"]
    fechacadu_vj=request.POST["fechacadu_vj"]
    precio_vj=request.POST["precio_vj"]
    if 'imagen_in_vj' in request.FILES:
            imagen_in_vj = request.FILES.get("imagen_in_vj")
    else:
            # Si no se proporciona una nueva imagen, conserva la existente
            in_existente = Ingrediente.objects.get(id_in_vj=id_in_vj)
            imagen_in_vj = in_existente.imagen_in_vj
    #Insertando datos mediante el ORM de DJANGO
    ingredienteEditar=Ingrediente.objects.get(id_in_vj=id_in_vj)
    ingredienteEditar.nombre_vj=nombre_vj
    ingredienteEditar.categoria_vj=categoria_vj
    ingredienteEditar.fechacadu_vj=fechacadu_vj
    ingredienteEditar.precio_vj=precio_vj
    ingredienteEditar.imagen_in_vj=imagen_in_vj
    ingredienteEditar.save()
    messages.success(request,
      'Ingrediente ACTUALIZADO Exitosamente')
    return redirect('/ingrediente')

def cliente(request):
    clientes=Cliente.objects.all()
    provincias=Provincia.objects.all()
    return render(request,'cliente.html',{'clientes':clientes, 'provincias': provincias,'navbar': 'cliente'})

def guardarCliente(request):
    id_provi=request.POST["id_provi"]
    provinciaSeleccionado=Provincia.objects.get(id_pro_vj=id_provi)
    cedula_vj=request.POST["cedula_vj"]
    apellido_vj=request.POST["apellido_vj"]
    nombre_vj=request.POST["nombre_vj"]
    direccion_vj=request.POST["direccion_vj"]


    nuevoCliente=Cliente.objects.create(cedula_vj=cedula_vj, apellido_vj=apellido_vj, nombre_vj=nombre_vj,
                                          direccion_vj=direccion_vj, provincia_vj=provinciaSeleccionado)
    return redirect('/cliente')

def eliminarCliente(request,id_cli_vj):
    clienteEliminar=Cliente.objects.get(id_cli_vj=id_cli_vj)
    clienteEliminar.delete()
    messages.success(request, 'Cliente eliminado exitosamente')
    return redirect('/cliente')

def editarCliente(request, id_cli_vj):
    clienteEditar=Cliente.objects.get(id_cli_vj=id_cli_vj)
    provincias=Provincia.objects.all()
    return render(request, 'editarCliente.html', {'cliente': clienteEditar, 'provincias': provincias})

def procesarinformacionCliente(request):
    id_cli_vj=request.POST["id_cli_vj"]
    id_provi=request.POST["id_provi"]
    provinciaSeleccionado=Provincia.objects.get(id_pro_vj=id_provi)
    cedula_vj=request.POST["cedula_vj"]
    apellido_vj=request.POST["apellido_vj"]
    nombre_vj=request.POST["nombre_vj"]
    direccion_vj=request.POST["direccion_vj"]
    #Insertando datos mediante el ORM de DJANGO
    clienteEditar=Cliente.objects.get(id_cli_vj=id_cli_vj)
    clienteEditar.provincia_vj=provinciaSeleccionado
    clienteEditar.cedula_vj=cedula_vj
    clienteEditar.apellido_vj=apellido_vj
    clienteEditar.nombre_vj=nombre_vj
    clienteEditar.direccion_vj=direccion_vj
    clienteEditar.save()
    messages.success(request,
      'Cliente ACTUALIZADO Exitosamente')
    return redirect('/cliente')


def pedido(request):
    pedidos=Pedido.objects.all()
    clientes=Cliente.objects.all()
    return render(request,'pedido.html',{'pedidos':pedidos, 'clientes': clientes,'navbar': 'pedido'})

def guardarPedido(request):
    id_cli=request.POST["id_cli"]
    pedidoSeleccionado=Cliente.objects.get(id_cli_vj=id_cli)
    fechape_vj=request.POST["fechape_vj"]
    estadope_vj=request.POST["estadope_vj"]
    metodopago_vj=request.POST["metodopago_vj"]
    observacion_vj=request.POST["observacion_vj"]


    nuevoPedido=Pedido.objects.create(fechape_vj=fechape_vj, estadope_vj=estadope_vj, metodopago_vj=metodopago_vj,
                                          observacion_vj=observacion_vj, cliente_vj=pedidoSeleccionado)
    return redirect('/pedido')

def eliminarPedido(request,id_pe_vj):
    pedidoEliminar=Pedido.objects.get(id_pe_vj=id_pe_vj)
    pedidoEliminar.delete()
    messages.success(request, 'Pedido eliminado exitosamente')
    return redirect('/pedido')

def editarPedido(request, id_pe_vj):
    pedidoEditar=Pedido.objects.get(id_pe_vj=id_pe_vj)
    clientes=Cliente.objects.all()
    return render(request, 'editarPedido.html', {'pedido': pedidoEditar, 'clientes': clientes})

def procesarinformacionPedido(request):
    id_pe_vj=request.POST["id_pe_vj"]
    id_cli=request.POST["id_cli"]
    pedidoSeleccionado=Cliente.objects.get(id_cli_vj=id_cli)
    fechape_vj=request.POST["fechape_vj"]
    estadope_vj=request.POST["estadope_vj"]
    metodopago_vj=request.POST["metodopago_vj"]
    observacion_vj=request.POST["observacion_vj"]
    #Insertando datos mediante el ORM de DJANGO
    pedidoEditar=Pedido.objects.get(id_pe_vj=id_pe_vj)
    pedidoEditar.cliente_vj=pedidoSeleccionado
    pedidoEditar.fechape_vj=fechape_vj
    pedidoEditar.estadope_vj=estadope_vj
    pedidoEditar.metodopago_vj=metodopago_vj
    pedidoEditar.observacion_vj=observacion_vj
    pedidoEditar.save()
    messages.success(request,
      'Pedido ACTUALIZADO Exitosamente')
    return redirect('/pedido')


def tipo(request):
    tipos=Tipo.objects.all()
    return render(request,'tipo.html',{'tipos':tipos, 'navbar': 'tipo'})

def guardarTipo(request):
    nombre_vj=request.POST["nombre_vj"]
    descripcion_vj=request.POST["descripcion_vj"]
    categoria_vj=request.POST["categoria_vj"]


    nuevoTipo=Tipo.objects.create(nombre_vj=nombre_vj, descripcion_vj=descripcion_vj, categoria_vj=categoria_vj)


    return redirect('/tipo')

def eliminarTipo(request,id_ti_vj):
    tipoEliminar=Tipo.objects.get(id_ti_vj=id_ti_vj)
    tipoEliminar.delete()
    messages.success(request, 'Tipo eliminado exitosamente')
    return redirect('/tipo')

def editarTipo(request, id_ti_vj):
    tipoEditar=Tipo.objects.get(id_ti_vj=id_ti_vj)
    return render(request, 'editarTipo.html', {'tipo': tipoEditar})

def procesarinformacionTipo(request):
    id_ti_vj=request.POST["id_ti_vj"]
    nombre_vj=request.POST["nombre_vj"]
    descripcion_vj=request.POST["descripcion_vj"]
    categoria_vj=request.POST["categoria_vj"]
    #Insertando datos mediante el ORM de DJANGO
    tipoEditar=Tipo.objects.get(id_ti_vj=id_ti_vj)
    tipoEditar.nombre_vj=nombre_vj
    tipoEditar.descripcion_vj=descripcion_vj
    tipoEditar.categoria_vj=categoria_vj
    tipoEditar.save()
    messages.success(request,
      'Tipo ACTUALIZADO Exitosamente')
    return redirect('/tipo')

def platillo(request):
    platillos=Platillo.objects.all()
    tipos=Tipo.objects.all()
    return render(request,'platillo.html',{'platillos':platillos, 'tipos': tipos,'navbar': 'tipo'})

def guardarPlatillo(request):
    id_tipo=request.POST["id_tipo"]
    tipoSeleccionado=Tipo.objects.get(id_ti_vj=id_tipo)
    nombre_vj=request.POST["nombre_vj"]
    calorias_vj=request.POST["calorias_vj"]
    descripcion_vj=request.POST["descripcion_vj"]
    imagen_pla_vj=request.FILES.get("imagen_pla_vj")


    nuevoPlatillo=Platillo.objects.create(nombre_vj=nombre_vj, calorias_vj=calorias_vj, descripcion_vj=descripcion_vj,
                                          imagen_pla_vj=imagen_pla_vj, tipo_vj=tipoSeleccionado)
    return redirect('/platillo')

def eliminarPlatillo(request,id_pla_vj):
    platilloEliminar=Platillo.objects.get(id_pla_vj=id_pla_vj)
    platilloEliminar.delete()
    messages.success(request, 'Platillo eliminado exitosamente')
    return redirect('/platillo')

def editarPlatillo(request, id_pla_vj):
    platilloEditar=Platillo.objects.get(id_pla_vj=id_pla_vj)
    tipos=Tipo.objects.all()
    return render(request, 'editarPlatillo.html', {'platillo': platilloEditar, 'tipos': tipos})

def procesarinformacionPlatillo(request):
    id_pla_vj=request.POST["id_pla_vj"]
    id_tipo=request.POST["id_tipo"]
    tipoSeleccionado=Tipo.objects.get(id_ti_vj=id_tipo)
    nombre_vj=request.POST["nombre_vj"]
    calorias_vj=request.POST["calorias_vj"]
    descripcion_vj=request.POST["descripcion_vj"]
    if 'imagen_pla_vj' in request.FILES:
            imagen_pla_vj = request.FILES.get("imagen_pla_vj")
    else:
            # Si no se proporciona una nueva imagen, conserva la existente
            in_existente = Platillo.objects.get(id_pla_vj=id_pla_vj)
            imagen_pla_vj = in_existente.imagen_pla_vj
    #Insertando datos mediante el ORM de DJANGO
    platilloEditar=Platillo.objects.get(id_pla_vj=id_pla_vj)
    platilloEditar.tipo_vj=tipoSeleccionado
    platilloEditar.nombre_vj=nombre_vj
    platilloEditar.calorias_vj=calorias_vj
    platilloEditar.descripcion_vj=descripcion_vj
    platilloEditar.imagen_pla_vj=imagen_pla_vj
    platilloEditar.save()
    messages.success(request,
      'Platillo ACTUALIZADO Exitosamente')
    return redirect('/platillo')


def detalle(request):
    detalles=Detalle.objects.all()
    pedidos=Pedido.objects.all()
    platillos=Platillo.objects.all()
    return render(request,'detalle.html',{'detalles':detalles, 'pedidos': pedidos, 'platillos': platillos, 'navbar': 'detalle'})

def guardarDetalle(request):
    id_pedido=request.POST["id_pedido"]
    id_platillo=request.POST["id_platillo"]
    detalleSeleccionado=Pedido.objects.get(id_pe_vj=id_pedido)
    deSeleccionado=Platillo.objects.get(id_pla_vj=id_platillo)
    cantidad_vj=request.POST["cantidad_vj"]
    preciounitario_vj=request.POST["preciounitario_vj"]
    descuento_vj=request.POST["descuento_vj"]
    total_vj=request.POST["total_vj"]


    nuevoDetalle=Detalle.objects.create(cantidad_vj=cantidad_vj, preciounitario_vj=preciounitario_vj, descuento_vj=descuento_vj,
                                          total_vj=total_vj, pedido_vj=detalleSeleccionado, platillo_vj=deSeleccionado)
    return redirect('/detalle')

def eliminarDetalle(request,id_de_vj):
    detalleEliminar=Detalle.objects.get(id_de_vj=id_de_vj)
    detalleEliminar.delete()
    messages.success(request, 'Detalle eliminado exitosamente')
    return redirect('/detalle')

def editarDetalle(request, id_de_vj):
    detalleEditar=Detalle.objects.get(id_de_vj=id_de_vj)
    pedidos=Pedido.objects.all()
    platillos=Platillo.objects.all()
    return render(request, 'editarDetalle.html', {'detalle': detalleEditar, 'pedidos': pedidos, 'platillos': platillos})

def procesarinformacionDetalle(request):
    id_de_vj=request.POST["id_de_vj"]
    id_pedido=request.POST["id_pedido"]
    id_platillo=request.POST["id_platillo"]
    detalleSeleccionado=Pedido.objects.get(id_pe_vj=id_pedido)
    deSeleccionado=Platillo.objects.get(id_pla_vj=id_platillo)
    cantidad_vj=request.POST["cantidad_vj"]
    preciounitario_vj=request.POST["preciounitario_vj"]
    descuento_vj=request.POST["descuento_vj"]
    total_vj=request.POST["total_vj"]

    #Insertando datos mediante el ORM de DJANGO
    detalleEditar=Detalle.objects.get(id_de_vj=id_de_vj)
    detalleEditar.pedido_vj=detalleSeleccionado
    detalleEditar.platillo_vj=deSeleccionado
    detalleEditar.cantidad_vj=cantidad_vj
    detalleEditar.preciounitario_vj=preciounitario_vj
    detalleEditar.descuento_vj=descuento_vj
    detalleEditar.total_vj=total_vj
    detalleEditar.save()
    messages.success(request,
      'Detalle ACTUALIZADO Exitosamente')
    return redirect('/detalle')


def receta(request):
    recetas=Receta.objects.all()
    platillos=Platillo.objects.all()
    ingredientes=Ingrediente.objects.all()
    return render(request,'receta.html',{'recetas':recetas, 'platillos': platillos, 'ingredientes': ingredientes, 'navbar': 'receta'})

def guardarReceta(request):
    id_platillo=request.POST["id_platillo"]
    id_ingrediente=request.POST["id_ingrediente"]
    recetaSeleccionado=Platillo.objects.get(id_pla_vj=id_platillo)
    reSeleccionado=Ingrediente.objects.get(id_in_vj=id_ingrediente)
    nombre_vj=request.POST["nombre_vj"]
    tiempoprepa_vj=request.POST["tiempoprepa_vj"]
    dificultad_vj=request.POST["dificultad_vj"]
    descripcion_vj=request.POST["descripcion_vj"]


    nuevoReceta=Receta.objects.create(nombre_vj=nombre_vj, tiempoprepa_vj=tiempoprepa_vj, dificultad_vj=dificultad_vj,
                                          descripcion_vj=descripcion_vj, platillo_vj=recetaSeleccionado, ingrediente_vj=reSeleccionado)
    return redirect('/receta')

def eliminarReceta(request,id_re_vj):
    recetaEliminar=Receta.objects.get(id_re_vj=id_re_vj)
    recetaEliminar.delete()
    messages.success(request, 'Receta eliminado exitosamente')
    return redirect('/receta')

def editarReceta(request, id_re_vj):
    recetaEditar=Receta.objects.get(id_re_vj=id_re_vj)
    platillos=Platillo.objects.all()
    ingredientes=Ingrediente.objects.all()
    return render(request, 'editarReceta.html', {'receta': recetaEditar, 'platillos': platillos, 'ingredientes': ingredientes})

def procesarinformacionReceta(request):
    id_re_vj=request.POST["id_re_vj"]
    id_platillo=request.POST["id_platillo"]
    id_ingrediente=request.POST["id_ingrediente"]
    recetaSeleccionado=Platillo.objects.get(id_pla_vj=id_platillo)
    reSeleccionado=Ingrediente.objects.get(id_in_vj=id_ingrediente)
    nombre_vj=request.POST["nombre_vj"]
    tiempoprepa_vj=request.POST["tiempoprepa_vj"]
    dificultad_vj=request.POST["dificultad_vj"]
    descripcion_vj=request.POST["descripcion_vj"]

    #Insertando datos mediante el ORM de DJANGO
    recetaEditar=Receta.objects.get(id_re_vj=id_re_vj)
    recetaEditar.platillo_vj=recetaSeleccionado
    recetaEditar.ingrediente_vj=reSeleccionado
    recetaEditar.nombre_vj=nombre_vj
    recetaEditar.tiempoprepa_vj=tiempoprepa_vj
    recetaEditar.dificultad_vj=dificultad_vj
    recetaEditar.descripcion_vj=descripcion_vj
    recetaEditar.save()
    messages.success(request,
      'Receta ACTUALIZADO Exitosamente')
    return redirect('/receta')
