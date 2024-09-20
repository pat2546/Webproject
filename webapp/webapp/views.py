from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Login view
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # ใช้ auth_login เพื่อไม่ชนกับฟังก์ชัน login ของ Django
            return redirect('login')  # เปลี่ยน 'home' เป็นชื่อ URL ของหน้าแรกของคุณ
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
            return redirect('login')  # เปลี่ยน 'login' เป็นชื่อ URL ของหน้า login ของคุณ
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Logout view
def user_logout(request):
    auth_logout(request)  # ใช้ auth_logout เพื่อไม่ชนกับฟังก์ชัน logout ของ Django
    return redirect('login')  # เปลี่ยน 'login' เป็นชื่อ URL ของหน้า login ของคุณ
