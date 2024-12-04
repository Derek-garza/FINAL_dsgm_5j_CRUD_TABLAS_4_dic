from django.shortcuts import render, redirect
from .models import Producto

def inicio_vistaProductos(request):
    los_productos = Producto.objects.all()
    return render(request, "gestionarProducto.html", {"mis_productos": los_productos})

def registrarProducto(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    peso = request.POST["txtpeso"]
    precio = request.POST["txtprecio"]
    stock = request.POST['numstock']
    id_producto = request.POST["txtid_producto"]
    calidad = request.POST["txtcalidad"]
    id_sucursal = request.POST['idsucursal']
    id_provedor = request.POST['idprovedor']

    Producto.objects.create(
        codigo=codigo,
        nombre=nombre,
        peso=peso,
        precio=precio,
        stock=stock,
        id_producto=id_producto,
        calidad=calidad,
        id_sucursal=id_sucursal,
        id_provedor=id_provedor
    )
    return redirect("productos")

def seleccionarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    return render(request, "editarProducto.html", {"mi_producto": producto})

def editarProducto(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    peso = request.POST["txtpeso"]
    precio = request.POST["txtprecio"]
    stock = request.POST['numstock']
    id_producto = request.POST["txtid_producto"]
    calidad = request.POST["txtcalidad"]
    id_sucursal = request.POST['idsucursal']
    id_provedor = request.POST['idprovedor']

    producto = Producto.objects.get(codigo=codigo)
    producto.nombre = nombre
    producto.peso = peso
    producto.precio = precio
    producto.stock=stock
    producto.id_producto = id_producto
    producto.calidad = calidad
    producto.id_sucursal=id_sucursal
    producto.id_provedor=id_provedor
    producto.save()
    return redirect("productos")

def borrarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()
    return redirect("productos")
