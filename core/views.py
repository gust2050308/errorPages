from django.shortcuts import render
from errorPages.forms import ContactoForm
from django.http import JsonResponse

#from alumno import alumno

# Create your views here.

def index(request):
    print("el usuario entro al sistema")

    return render(request, 'core/index.html')

def onePage(request):
    print("el usuario entro al sistema")

    return render(request, 'core/onePage.html')


def MejiaGustavo(request):
    print("el usuario entro al sistema")

    return render(request, 'core/MejiaGustavo.html')


# def nuevo(request):
#     variable = alumno("Gustavo", "Mejia", 20)
#     return render(request, 'core/nuevo.html', {'variable': variable})




def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Los datos ya pasaron las validaciones de front y back
            #registrar en la base de datos
            form.save()

            return JsonResponse({
                'status': 'ok',
                'message': 'Mensaje enviado correctamente'
            }, status=200)
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'Error al enviar el mensaje'
            }, status=400)

           
    else:
        form = ContactoForm()
    
    return render(request, 'core/formulario.html', {'form': form})
