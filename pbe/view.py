from django.http import HttpResponse

def bienvenida (request):
    return HttpResponse("bienvenido lunes 6 de mayo")



def calcula_edad (request,edad):
    if edad>=18:
        
        categoria="mayor o igual  de 18"
    else:
        categoria="menor de edad "


    result=f"<h1>la edad es{categoria}</h1>"
    return HttpResponse (result)



