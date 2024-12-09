from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required

def user_register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)  # Автоматичний вхід після реєстрації
        return redirect('profile')  # Перенаправлення на сторінку профілю
    return render(request, 'register.html', {'form': form})  # Відображення форми реєстрації

def user_login(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)  
        return redirect('profile')  
    return render(request, 'login.html', {'form': form})  

def user_logOut(request):
    logout(request)  
    return redirect('index')  

@login_required
def user_check_profile(request):
    return render(request, 'profile.html')  
