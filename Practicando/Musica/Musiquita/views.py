from django.shortcuts import render

def primera(request): #El request es la petición, render pinta mi templates

    templates = 'Musiquita/Inicio.html'

    return render(request,templates)

def segunda(request): #El request es la petición, render pinta mi templates

    templates = 'Musiquita/Secundario.html'

    return render(request,templates)

def login(request): #El request es la petición, render pinta mi templates

    templates = 'Musiquita/Login.html'

    return render(request,templates)
def formulario(request): #El request es la petición, render pinta mi templates

    templates = 'Musiquita/Formulario.html'

    return render(request,templates)
def admin(request):

    templates = 'Musiquita/Admin.html'

    return render(request,templates)

def agregarcanciones(request):

    templates = 'Musiquita/AgregarCanciones.html'

    return render(request,templates)

def agregarartistas(request):

    templates = 'Musiquita/AgregarArtistas.html'

    return render(request,templates)

def linkeimagen(request):

    templates = 'Musiquita/LinkeImagen.html'

    return render(request,templates)
# Create your views here.

