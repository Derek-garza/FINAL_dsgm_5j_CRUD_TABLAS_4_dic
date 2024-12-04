from django.shortcuts import render, redirect
from .models import Sucursal

# Create your views here.
def inicio_vistaSucursal(request):
    lassucursales = Sucursal.objects.all()
    return render(request, "gestionarSucursal.html", {"missucursales": lassucursales})

def registrarSucursal(request):
    id_sucursal = request.POST["txtcodigo"]
    nombre_sucursal = request.POST["txtnombre"]
    calle_sucursal = request.POST["txtcalle"]
    num_empleados = request.POST["txtempleados"]
    tel_sucursal = request.POST["txttelefono"]

    Sucursal.objects.create(
        id_sucursal=id_sucursal,
        nombre_sucursal=nombre_sucursal,
        calle_sucursal=calle_sucursal,
        num_empleados=num_empleados,
        tel_sucursal=tel_sucursal,
    )

    return redirect("sucursal")

def seleccionarSucursal(request, codigo):
    sucursal = Sucursal.objects.get(id_sucursal=codigo)
    return render(request, "editarSucursal.html", {"missucursales": sucursal})

def editarSucursal(request):
    id_sucursal = request.POST["txtcodigo"]
    nombre_sucursal = request.POST["txtnombre"]
    calle_sucursal = request.POST["txtcalle"]
    num_empleados = request.POST["txtempleados"]
    tel_sucursal = request.POST["txttelefono"]

    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.nombre_sucursal = nombre_sucursal
    sucursal.calle_sucursal = calle_sucursal
    sucursal.num_empleados = num_empleados
    sucursal.tel_sucursal = tel_sucursal

    sucursal.save()
    return redirect("sucursal")

def borrarSucursal(request, codigo):
    sucursal = Sucursal.objects.get(id_sucursal=codigo)
    sucursal.delete()
    return redirect("sucursal")
