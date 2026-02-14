# Error Pages - Sistema de Reportes de Errores

Sistema web desarrollado con Django para gestionar y reportar errores de aplicaciones.

## 🚀 Características

- ✅ Formulario de reporte de errores
- ✅ Visualización de reportes en tabla interactiva
- ✅ Interfaz moderna con Tailwind CSS
- ✅ Diseño responsive (móvil y desktop)
- ✅ Badges de colores según tipo de error (4xx, 5xx)
- ✅ Sistema de navegación intuitivo

## 🛠️ Tecnologías

- **Backend**: Django 6.0.1
- **Frontend**: Tailwind CSS
- **Base de datos**: SQLite (desarrollo)
- **Python**: 3.13.7

## 📋 Requisitos

- Python 3.13+
- pip

## 🔧 Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/TU_USUARIO/errorPages.git
cd errorPages
```

2. **Crear entorno virtual**
```bash
python -m venv venv
```

3. **Activar entorno virtual**
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

5. **Ejecutar migraciones**
```bash
python manage.py migrate
```

6. **Crear superusuario (opcional)**
```bash
python manage.py createsuperuser
```

7. **Ejecutar servidor de desarrollo**
```bash
python manage.py runserver
```

8. **Abrir en navegador**
```
http://127.0.0.1:8000/
```

## 📁 Estructura del Proyecto

```
errorPages/
├── core/                   # App principal
├── error_reports/          # App de reportes de errores
│   ├── models.py          # Modelo ErrorReport
│   ├── views.py           # Vistas de reportes
│   ├── forms.py           # Formularios
│   └── templates/         # Templates
├── errorPages/            # Configuración del proyecto
├── templates/             # Templates base
│   └── base.html         # Template base con navbar
└── manage.py
```

## 🎨 Páginas

- `/` - Página de inicio
- `/reporte/` - Formulario para reportar errores
- `/errorReports/` - Tabla de reportes de errores
- `/formulario/` - Formulario de contacto

## 📝 Licencia

Este proyecto es de código abierto.

## 👤 Autor

Gustavo Mejía
