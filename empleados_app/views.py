from django.shortcuts import render, redirect
from .models import Empleado

def inicio_vistaEmpleados(request):
    los_empleados = Empleado.objects.all()
    return render(request, "gestionarEmpleado.html", {"mis_empleados": los_empleados})

def registrarEmpleado(request):
    id_empleado = request.POST["txtcodigo"]
    curp = request.POST["txtcurp"]
    telefono = request.POST["txttelefono"]
    direccion = request.POST["txtdireccion"]
    nombre = request.POST["txtnombre"]
    fecha_nac = request.POST["txtedad"]
    sexo = request.POST["txtsexo"]
    id_sucursal = request.POST['txtsucusal']

    Empleado.objects.create(
        id_empleado=id_empleado,
        curp=curp,
        telefono=telefono,
        direccion=direccion,
        nombre=nombre,
        fecha_nac=fecha_nac,
        sexo=sexo,
        id_sucursal=id_sucursal
    )
    return redirect("empleados")

def seleccionarEmpleado(request, codigo):
    empleado = Empleado.objects.get(id_empleado=codigo)
    fecha_nac = empleado.fecha_nac.strftime('%Y-%m-%d')
    return render(request, "editarEmpleado.html", {"mi_empleado": empleado, "fecha_nac": fecha_nac})

def editarEmpleado(request):
    id_empleado = request.POST["txtcodigo"]
    curp = request.POST["txtcurp"]
    telefono = request.POST["txttelefono"]
    direccion = request.POST["txtdireccion"]
    nombre = request.POST["txtnombre"]
    fecha_nac = request.POST["txtedad"]
    sexo = request.POST["txtsexo"]
    id_sucursal = request.POST['txtsucusal']

    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.curp = curp
    empleado.telefono = telefono
    empleado.direccion = direccion
    empleado.nombre = nombre
    empleado.fecha_nac = fecha_nac
    empleado.sexo = sexo
    empleado.id_sucursal=id_sucursal
    empleado.save()
    return redirect("empleados")

def borrarEmpleado(request, codigo):
    empleado = Empleado.objects.get(id_empleado=codigo)
    empleado.delete()
    return redirect("empleados")
