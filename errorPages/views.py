from django.shortcuts import render
from .forms import ContactoForm


def home(request):
    """Home page view"""
    return render(request, 'base.html')


def test_error(request):
    """Intentionally trigger a 500 error for testing"""
    # This will cause a server error
    result = 1 / 0  # ZeroDivisionError
    return render(request, 'base.html')


def contatco_view(request):
    form = ContactoForm()
    return render(request, 'core/formulario.html', {'form': form}) 