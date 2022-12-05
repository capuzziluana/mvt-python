from django.urls import path
from .views import Vistas
from .vistas import Saludo_view,Familiar_view

urlpatterns = [
    path("saludar",Saludo_view.saludar),
    path ('autogenerarlistafamiliares',Familiar_view.autogenerar_listar_familiares)
]