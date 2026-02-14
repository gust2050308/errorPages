from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ErrorReportForm
from .models import ErrorReport

# Create your views here.
def reporte_view(request):
    if request.method == 'POST':
        form = ErrorReportForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'ok', 'message': 'Reporte guardado correctamente'})
        else:
            return JsonResponse({'status': 'error', 'message': form.errors})
    else:
        form = ErrorReportForm()
    return render(request, 'reporte.html', {'form': form})

def errorReports_view(request):
    errorReports = ErrorReport.objects.all()
    
    # Si es una petición AJAX, devolver JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
        data = []
        for report in errorReports:
            data.append({
                'titulo': report.titulo,
                'descripcion': report.descripcion,
                'tipo_error': report.tipo_error,
                'url': report.url,
                'metodo_http': report.metodo_http,
                'ip_cliente': report.ip_cliente,
                'fecha_reporte': report.fecha_reporte.strftime('%Y-%m-%d %H:%M:%S'),
                'activo': report.activo
            })
        return JsonResponse(data, safe=False)
    
    # Si es una petición normal, devolver HTML
    return render(request, 'errorReports.html', {'errorReports': errorReports})
