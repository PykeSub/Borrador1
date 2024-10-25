from django.shortcuts import render, redirect
from distribuidorApp.models import Distribuidores
from distribuidorApp.forms import FormDistribuidor

# Create your views here.

def index(request):
    return render(request, 'distribuidorApp/index.html')

def listadoDistribuidor(request):
    distribuidores = Distribuidores.objects.all()
    data = {'distribuidores' : distribuidores}
    return render(request, 'distribuidorApp/distribuidor.html', data)

def agregarDistribuidor(request):
    form = FormDistribuidor
    if request.method == 'POST':
        form = FormDistribuidor(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'distribuidorApp/agregarDistribuidor.html', data)

def eliminarDistribuidor(request, id):
    distribuidor = Distribuidores.objects.get(id = id)
    distribuidor.delete()
    return redirect('/distribuidores')

def actualizarDistribuidor(request, id):
    distribuidor = Distribuidores.objects.get(id = id)
    form = FormDistribuidor(intance = distribuidor)
    if request.method == 'POST':
        form = FormDistribuidor(request.POST, instance = distribuidor)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'distribuidorApp/agregarDistribuidor.html', data)