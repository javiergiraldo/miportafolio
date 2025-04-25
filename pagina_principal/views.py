from django.shortcuts import render

def inicio(request):
    return render(request, 'pagina_principal/inicio.html')

def proyectos(request):
    return render(request, 'pagina_principal/proyectos.html')

def sobre_mi(request):
    return render(request, 'pagina_principal/sobre_mi.html')

def contacto(request):
    return render(request, 'pagina_principal/contacto.html')