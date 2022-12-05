from django.shortcuts import render

class Saludo_view:
    def saludar(request):
        return render(request, "saludar.html")
