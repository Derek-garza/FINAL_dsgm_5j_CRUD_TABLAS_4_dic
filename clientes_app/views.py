from django.shortcuts import render, redirect
from .models import Cliente

# Create your views here.
def inicio_vistaCliente(request):
    losclientes = Cliente.objects.all()
    return render(request, "gestionarCliente.html", {"misclientes": losclientes})

def registrarCliente(request):
    id_cliente = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    fecha_nacimiento = request.POST["txtfecha"]
    correo = request.POST["txtcorreo"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["txttelefono"]
    codigo_p = request.POST["txtcodigo_p"]

    Cliente.objects.create(
        id_cliente=id_cliente,
        nombre=nombre,
        fecha_nacimiento=fecha_nacimiento,
        correo=correo,
        direccion=direccion,
        telefono=telefono,
        codigo_p=codigo_p,
    )

    return redirect("cliente")

def seleccionarCliente(request, codigo):
    cliente = Cliente.objects.get(id_cliente=codigo)
    fecha_nacimiento=cliente.fecha_nacimiento.strftime('%Y-%m-%d')
    return render(request,"editarCliente.html",{"misclientes":cliente, "misclientes" : cliente, "fecha_nacimiento" : fecha_nacimiento})

def editarCliente(request):
    id_cliente = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    fecha_nacimiento = request.POST["txtfecha"]
    correo = request.POST["txtcorreo"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["txttelefono"]
    codigo_p = request.POST["txtcodigo_p"]

    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre = nombre
    cliente.fecha_nacimiento = fecha_nacimiento
    cliente.correo = correo
    cliente.direccion = direccion
    cliente.telefono = telefono
    cliente.codigo_p = codigo_p

    cliente.save()
    return redirect("cliente")

def borrarCliente(request, codigo):
    cliente = Cliente.objects.get(id_cliente=codigo)
    cliente.delete()
    return redirect("cliente")
