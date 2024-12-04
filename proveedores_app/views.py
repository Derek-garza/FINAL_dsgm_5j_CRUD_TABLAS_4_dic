from django.shortcuts import render, redirect
from .models import Proveedor

# Create your views here.
def inicio_vistaProveedor(request):
    losproveedores = Proveedor.objects.all()
    return render(request, "gestionarProveedor.html", {"misproveedores": losproveedores})

def registrarProveedor(request):
    id_proveedor = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    producto = request.POST["txtproducto"]
    direccion = request.POST["txtdireccion"]
    id_sucursal = request.POST["txtsucursal"]

    Proveedor.objects.create(
        id_proveedor=id_proveedor,
        nombre=nombre,
        telefono=telefono,
        producto=producto,
        direccion=direccion,
        id_sucursal=id_sucursal,
    )

    return redirect("proveedor")

def seleccionarProveedor(request, codigo):
    proveedor = Proveedor.objects.get(id_proveedor=codigo)
    return render(request, "editarProveedor.html", {"misproveedores": proveedor})

def editarProveedor(request):
    id_proveedor = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    producto = request.POST["txtproducto"]
    direccion = request.POST["txtdireccion"]
    id_sucursal = request.POST["txtsucursal"]

    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.nombre = nombre
    proveedor.telefono = telefono
    proveedor.producto = producto
    proveedor.direccion = direccion
    proveedor.id_sucursal = id_sucursal

    proveedor.save()
    return redirect("proveedor")

def borrarProveedor(request, codigo):
    proveedor = Proveedor.objects.get(id_proveedor=codigo)
    proveedor.delete()
    return redirect("proveedor")
