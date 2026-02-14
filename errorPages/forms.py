
from django import forms
from django.core.exceptions import ValidationError
from core.models import Contacto
from error_reports.models import ErrorReport


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'mensaje']

