from django.shortcuts import render, redirect
from .models import Venta

def inicio_vistaVentas(request):
    las_ventas = Venta.objects.all()
    return render(request, "gestionarVenta.html", {"mis_ventas": las_ventas})

def registrarVenta(request):
    id_venta = request.POST["txtid_venta"]
    id_empleado = request.POST["txtid_empleado"]
    id_cliente = request.POST["txtid_cliente"]
    id_producto = request.POST["txtid_producto"]
    fecha_venta = request.POST["txtfecha_venta"]
    cantidad = request.POST["txtcantidad"]
    id_sucursal = request.POST["txtid_sucursal"]

    Venta.objects.create(
        id_venta=id_venta,
        id_empleado=id_empleado,
        id_cliente=id_cliente,
        id_producto=id_producto,
        fecha_venta=fecha_venta,
        cantidad=cantidad,
        id_sucursal=id_sucursal,
    )
    return redirect("ventas")

def seleccionarVenta(request, id_venta):
    venta = Venta.objects.get(id_venta=id_venta)
    fecha_venta=venta.fecha_venta.strftime('%Y-%m-%d')
    return render(request,"editarVenta.html",{"mi_venta":venta, "mi_venta" : venta, "fecha_venta" : fecha_venta})

def editarVenta(request):
    id_venta = request.POST["txtid_venta"]
    id_empleado = request.POST["txtid_empleado"]
    id_cliente = request.POST["txtid_cliente"]
    id_producto = request.POST["txtid_producto"]
    fecha_venta = request.POST["txtfecha_venta"]
    cantidad = request.POST["txtcantidad"]
    id_sucursal = request.POST["txtid_sucursal"]

    venta = Venta.objects.get(id_venta=id_venta)
    venta.id_empleado = id_empleado
    venta.id_cliente = id_cliente
    venta.id_producto = id_producto
    venta.fecha_venta = fecha_venta
    venta.cantidad = cantidad
    venta.id_sucursal = id_sucursal
    venta.save()
    return redirect("ventas")

def borrarVenta(request, id_venta):
    venta = Venta.objects.get(id_venta=id_venta)
    venta.delete()
    return redirect("ventas")
