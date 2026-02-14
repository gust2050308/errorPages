---
description: Understanding Django Architecture (for Next.js developers)
---

# Django Architecture Guide (Coming from Next.js)

Since you know Next.js, I'll explain Django by comparing it to concepts you're already familiar with.

## 🏗️ Django vs Next.js Architecture

### **Next.js (What you know)**
- **Full-stack framework** with frontend (React) + backend (API routes)
- File-based routing in `app/` or `pages/`
- Components generate UI
- API routes handle backend logic
- Built-in server-side rendering

### **Django (Backend-focused)**
- **Backend framework** primarily for server-side logic
- URL routing defined in `urls.py` files
- Views handle logic (like API routes)
- Templates render HTML (like React components, but server-side)
- Python-based instead of JavaScript

---

## 📁 Project Structure Comparison

### Next.js Structure:
```
my-app/
├── app/
│   ├── page.tsx              # Home page
│   ├── about/page.tsx        # About page
│   └── api/users/route.ts    # API endpoint
├── components/
├── public/
└── package.json
```

### Django Structure:
```
myproject/
├── myproject/              # Project config folder
│   ├── settings.py        # Configuration (like next.config.js)
│   ├── urls.py            # Root URL routing
│   └── wsgi.py            # Server config
├── myapp/                 # App folder (like a feature module)
│   ├── models.py          # Database models
│   ├── views.py           # Request handlers (like API routes)
│   ├── urls.py            # App-specific routes
│   └── templates/         # HTML templates
├── templates/             # Global templates
├── static/                # CSS, JS, images (like public/)
└── manage.py              # CLI tool (like npm scripts)
```

---

## 🔑 Key Components

### 1️⃣ **Routing**

**Next.js:**
```typescript
// File-based routing
app/
  page.tsx          → /
  about/page.tsx    → /about
  blog/[id]/page.tsx → /blog/:id
```

**Django:**
```python
# urls.py - Explicit routing
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                    # /
    path('about/', views.about, name='about'),            # /about
    path('blog/<int:id>/', views.blog_detail),            # /blog/:id (dynamic)
    path('api/users/', views.api_users),                  # /api/users/
]
```

---

### 2️⃣ **Handlers (Views vs Route Handlers)**

**Next.js API Route:**
```typescript
// app/api/users/route.ts
export async function GET(request: Request) {
  const users = await db.users.findMany();
  return Response.json(users);
}

export async function POST(request: Request) {
  const body = await request.json();
  const user = await db.users.create(body);
  return Response.json(user);
}
```

**Django View:**
```python
# views.py
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Function-based view (most common)
def home(request):
    """Render HTML template"""
    return render(request, 'home.html', {'title': 'Home'})

def api_users(request):
    """API endpoint returning JSON"""
    if request.method == 'GET':
        users = User.objects.all()
        return JsonResponse({'users': list(users.values())})
    
    elif request.method == 'POST':
        data = request.POST  # or json.loads(request.body)
        user = User.objects.create(**data)
        return JsonResponse({'user': user.id})

# Class-based view (alternative)
from django.views import View

class UserView(View):
    def get(self, request):
        users = User.objects.all()
        return JsonResponse({'users': list(users.values())})
    
    def post(self, request):
        # Handle POST
        pass
```

---

### 3️⃣ **Templates (Django Templates vs React Components)**

**Next.js Component:**
```tsx
// components/UserCard.tsx
export default function UserCard({ name, email }: Props) {
  return (
    <div className="card">
      <h2>{name}</h2>
      <p>{email}</p>
    </div>
  );
}

// app/page.tsx
export default function Page() {
  return <UserCard name="John" email="john@example.com" />;
}
```

**Django Template:**
```django
<!-- templates/user_card.html -->
<div class="card">
  <h2>{{ name }}</h2>
  <p>{{ email }}</p>
</div>

<!-- templates/home.html -->
{% include 'user_card.html' with name="John" email="john@example.com" %}

<!-- OR with loops (like .map() in React) -->
{% for user in users %}
  <div class="card">
    <h2>{{ user.name }}</h2>
    <p>{{ user.email }}</p>
  </div>
{% endfor %}

<!-- Conditionals (like ternary in React) -->
{% if user.is_active %}
  <span>Active</span>
{% else %}
  <span>Inactive</span>
{% endif %}
```

**Passing data to templates (like props):**
```python
# views.py
def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {
        'users': users,        # Like passing props
        'title': 'User List',
    })
```

---

### 4️⃣ **Database / Models (Django ORM vs Prisma)**

**Next.js with Prisma:**
```typescript
// prisma/schema.prisma
model User {
  id    Int    @id @default(autoincrement())
  name  String
  email String @unique
}

// Usage
const users = await prisma.user.findMany();
const user = await prisma.user.create({
  data: { name: 'John', email: 'john@example.com' }
});
```

**Django Models:**
```python
# models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

# Usage in views.py
users = User.objects.all()                    # Get all users
user = User.objects.get(id=1)                 # Get one user
user = User.objects.create(                   # Create user
    name='John',
    email='john@example.com'
)
user = User.objects.filter(name='John')       # Filter users
```

**Creating tables (migrations):**
```bash
# Like "prisma migrate dev"
python manage.py makemigrations    # Create migration files
python manage.py migrate           # Apply migrations to database
```

---

### 5️⃣ **Configuration (settings.py vs next.config.js)**

**Next.js:**
```typescript
// next.config.js
module.exports = {
  env: {
    API_URL: 'https://api.example.com',
  },
  images: {
    domains: ['example.com'],
  },
}
```

**Django:**
```python
# settings.py
DEBUG = True  # Like development mode
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',  # Built-in admin panel
    'django.contrib.auth',   # Built-in authentication
    'myapp',                 # Your app
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Template directories
    },
]

STATIC_URL = '/static/'  # Like public/ folder
```

---

## 🔄 Request Flow Comparison

### **Next.js Request Flow:**
```
Browser → Route (page.tsx or api/route.ts) → Component/Handler → Response
```

### **Django Request Flow:**
```
Browser → urls.py (routing) → views.py (handler) → template/JSON → Response
```

**Example Django Flow:**

1. User visits `/blog/5/`
2. Django checks `urls.py` and finds: `path('blog/<int:id>/', views.blog_detail)`
3. Calls `views.blog_detail(request, id=5)`
4. View fetches data from database and renders template
5. Returns HTML response to browser

---

## 📦 Apps vs Modules

**Next.js:**
- You organize code however you want (folders, components, etc.)

**Django:**
- Uses "Apps" as reusable modules
- Each app is self-contained with models, views, templates, urls

```bash
# Create a new app
python manage.py startapp blog

# Result:
blog/
├── models.py      # Database models
├── views.py       # Request handlers
├── urls.py        # Routes for this app
├── admin.py       # Admin panel config
└── templates/     # HTML templates
```

Then register it in `settings.py`:
```python
INSTALLED_APPS = [
    # ...
    'blog',  # Add your app
]
```

---

## 🛠️ Common Django Commands

| Django Command | Next.js Equivalent | Purpose |
|----------------|-------------------|---------|
| `python manage.py runserver` | `npm run dev` | Start development server |
| `python manage.py makemigrations` | `prisma migrate dev` | Create database migrations |
| `python manage.py migrate` | (auto in Prisma) | Apply migrations |
| `python manage.py createsuperuser` | - | Create admin user |
| `python manage.py shell` | `node` REPL | Interactive Python shell |
| `python manage.py startapp myapp` | - | Create new Django app |

---

## 🎨 Template Inheritance (Like Layout Components)

**Next.js Layout:**
```tsx
// app/layout.tsx
export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        <nav>...</nav>
        {children}
        <footer>...</footer>
      </body>
    </html>
  );
}
```

**Django Template Inheritance:**
```django
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <nav>...</nav>
    
    {% block content %}
    <!-- Page content goes here -->
    {% endblock %}
    
    <footer>...</footer>
</body>
</html>

<!-- templates/home.html -->
{% extends 'base.html' %}

{% block title %}Home - My Site{% endblock %}

{% block content %}
  <h1>Welcome Home!</h1>
  <p>This is the home page.</p>
{% endblock %}
```

---

## 🔐 Authentication

**Next.js:**
- Use NextAuth.js or custom solution

**Django:**
- Built-in authentication system!

```python
# views.py
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

# Protected view (like middleware in Next.js)
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # Only logged-in users can access
    return render(request, 'dashboard.html')
```

---

## 🎯 Key Differences Summary

| Feature | Next.js | Django |
|---------|---------|--------|
| **Language** | JavaScript/TypeScript | Python |
| **Routing** | File-based | Configuration-based (`urls.py`) |
| **Templates** | React/JSX | Django Template Language |
| **Focus** | Full-stack (frontend + API) | Backend (can do frontend too) |
| **Database** | External ORM (Prisma, etc.) | Built-in ORM |
| **Auth** | Third-party (NextAuth) | Built-in |
| **Admin Panel** | Build yourself | Built-in! |

---

## 🚀 Your Current Project Structure

Your `errorPages` project:

```
errorPages/
├── errorPages/           # Project config
│   ├── settings.py      # Configuration
│   ├── urls.py          # Routes: /, /test-500/, /admin/
│   └── views.py         # Request handlers
├── templates/           # HTML templates
│   ├── base.html       # Landing page
│   ├── 404.html        # Not Found error
│   └── 500.html        # Server error
├── db.sqlite3          # Database file
└── manage.py           # CLI tool
```

**URL Flow:**
1. User visits `/` → `urls.py` matches `path('', views.home)` → calls `views.home()` → renders `base.html`
2. User visits `/test-500/` → matches `path('test-500/', views.test_error)` → raises error → shows `500.html`
3. User visits `/random/` → no match → shows `404.html`

---

## 🎓 Learning Path

If you're comfortable with Next.js, Django will feel familiar:

1. **You already know:** HTTP, routing, request/response, databases
2. **New concepts:** Python syntax, Django ORM, template syntax
3. **Big advantage:** Django has TONS of built-in features (auth, admin, ORM)

The mental model is similar, just different syntax and conventions!
