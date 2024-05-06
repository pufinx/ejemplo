
from django.contrib import admin
from django.urls import path
from pbe.view import bienvenida,calcula_edad, datos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/',bienvenida),
    path('edad/<int:edad>',calcula_edad),
    path('datos/<int:edad>',datos),
    

]

