from django.shortcuts import render

# Create your views here.

class Vistas:
    def saludar(request):
        return render(request, "saludar.html")