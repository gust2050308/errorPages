"""
URL configuration for errorPages project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from error_reports import views as error_reports

from core import views as core

urlpatterns = [
    path('test-500/', views.test_error, name='test_error'),
    path('admin/', admin.site.urls),
    path('', core.index, name='index'),
    path('onePage/', core.onePage, name='carreras'),
    path('MejiaGustavo/', core.MejiaGustavo, name='MejiaGustavo'),
    path('formulario/', core.contacto_view, name='formulario'),
    path('reporte/', error_reports.reporte_view, name='reporte'),
    path('errorReports/', error_reports.errorReports_view, name='errorReports'),
]

