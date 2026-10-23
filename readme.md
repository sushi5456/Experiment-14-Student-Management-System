Yes, the answer provided above is correct and structured for inclusion in your manual. However, I will now refine and structure it properly for **Experiment 14: Student Management System using Django**, ensuring clarity and completeness for your manual.  

---

# **Experiment 14: Student Management System using Django**  

## **14.1 Aim**  
To develop a **Student Management System** using Django, implementing:  
✅ **User Registration & Login**  
✅ **Navigation (Contact & About Pages)**  
✅ **Django Routing for Page Navigation**  

---

## **14.2 Overview**  

### **What is a Student Management System?**  
A **Student Management System** is a web application that allows users to:  
- **Register** a new student account  
- **Login** using valid credentials  
- **Navigate to Contact & About pages** using Django Routing  

### **Why Use Django?**  
- **Built-in User Authentication** → Secure registration & login.  
- **Django Routing System** → Efficient page navigation.  
- **Django ORM** → Easy database handling.  

---

## **14.3 Steps to Implement**  

1️⃣ **Set Up Django Project & Application**  
2️⃣ **Configure URL Routing for Navigation**  
3️⃣ **Implement User Registration & Login**  
4️⃣ **Create Contact & About Pages**  
5️⃣ **Test the Application**  

---

## **14.4 Code Implementation**  

### **1️⃣ Set Up Django Project & Application**  

📌 **Install Django**  
```sh
pip install django
```

📌 **Create Django Project & App**  
```sh
django-admin startproject student_management
cd student_management
django-admin startapp students
```

📌 **Add `students` to `INSTALLED_APPS` in `settings.py`**  
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'students',
]
```

---

### **2️⃣ Configure URL Routing for Navigation**  

📌 **Modify `student_management/urls.py`:**  
```python
from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('logout/', views.logout_user, name='logout'),
]
```

---

### **3️⃣ Implement User Registration & Login**  

📌 **Modify `students/models.py`:**  
```python
from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()
```

📌 **Apply Migrations**  
```sh
python manage.py makemigrations
python manage.py migrate
```

📌 **Modify `students/forms.py`:**  
```python
from django import forms
from django.contrib.auth.models import User
from .models import StudentProfile

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['phone', 'address']
```

📌 **Modify `students/views.py`:**  
```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm, StudentProfileForm
from .models import StudentProfile

def home(request):
    return render(request, 'students/home.html')

def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        profile_form = StudentProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        user_form = RegisterForm()
        profile_form = StudentProfileForm()
    return render(request, 'students/register.html', {'user_form': user_form, 'profile_form': profile_form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'students/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def contact(request):
    return render(request, 'students/contact.html')

def about(request):
    return render(request, 'students/about.html')
```

---

### **4️⃣ Create Contact & About Pages**  

📌 **Create `templates/students/home.html`**  
```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h2>Welcome to Student Management System</h2>
    <a href="{% url 'register' %}">Register</a> | 
    <a href="{% url 'login' %}">Login</a> | 
    <a href="{% url 'contact' %}">Contact</a> | 
    <a href="{% url 'about' %}">About</a>
</body>
</html>
```

📌 **Create `templates/students/register.html`**  
```html
<form method="post">
    {% csrf_token %}
    {{ user_form.as_p }}
    {{ profile_form.as_p }}
    <button type="submit">Register</button>
</form>
```

📌 **Create `templates/students/login.html`**  
```html
<form method="post">
    {% csrf_token %}
    <input type="text" name="username" placeholder="Username">
    <input type="password" name="password" placeholder="Password">
    <button type="submit">Login</button>
</form>
```

📌 **Create `templates/students/contact.html`**  
```html
<h2>Contact Page</h2>
<p>Email: admin@university.com</p>
<p>Phone: +123456789</p>
```

📌 **Create `templates/students/about.html`**  
```html
<h2>About Page</h2>
<p>Student Management System built using Django.</p>
```

---

### **5️⃣ Test the Application**  

📌 **Run the Django Server**  
```sh
python manage.py runserver
```

📌 **Access the application in a browser:**  
- **Home Page:** `http://127.0.0.1:8000/`  
- **Registration Page:** `http://127.0.0.1:8000/register/`  
- **Login Page:** `http://127.0.0.1:8000/login/`  
- **Contact Page:** `http://127.0.0.1:8000/contact/`  
- **About Page:** `http://127.0.0.1:8000/about/`  

---

## **14.5 Expected Output**  

✅ **User successfully registers and logs in.**  
✅ **Navigation works between Home, Contact, and About pages.**  
✅ **Django handles routing and authentication properly.**  

---

## **14.6 Viva Questions**  
1️⃣ What is Django routing, and why is it important?  
2️⃣ How does Django handle user authentication?  
3️⃣ What is the difference between `redirect()` and `render()` in Django?  
4️⃣ How do you create a one-to-one relationship in Django models?  
5️⃣ How can you add custom validation in Django forms?  

