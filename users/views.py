from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail  # New import for sending emails
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes  # Use the recommended replacement for force_text
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages  # New import for showing messages

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматичний вхід після реєстрації
            current_site = get_current_site(request)
            mail_subject = 'Activate Your Account'
            message = render_to_string('activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            send_mail(mail_subject, message, 'admin@mydomain.com', [user.email])
            
            # Логування відправлення листа
            print(f'Activation email sent to {user.email}')

            messages.success(request, 'A confirmation email has been sent to your email address. Please check it to activate your account.')
            return redirect('login')  # Перенаправлення на сторінку логіна
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})  # Відображення форми реєстрації

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  
            return redirect('profile')  
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})  

def user_logOut(request):
    logout(request)  
    return redirect('index')  

@login_required
def user_check_profile(request):
    return render(request, 'profile.html')

def activate_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()  # Decode the uid
        user = User.objects.get(pk=uid)  # Get user by uid
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):  # Check token validity
        user.is_active = True  # Activate the account
        user.save()
        messages.success(request, 'Your account has been activated. You can now log in.')
        return redirect('login')  # Redirect to login page after activation
    else:
        return render(request, 'activation_invalid.html')  # Render an invalid token error page

def reset_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = authenticate(request, username=email)
        if user:
            current_site = get_current_site(request)
            mail_subject = 'Password Reset Request'
            message = render_to_string('password_reset_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            send_mail(mail_subject, message, 'admin@mydomain.com', [email])
            
            # Логування відправлення листа
            print(f'Password reset email sent to {email}')

            messages.success(request, 'A password reset email has been sent to your email address.')
            return redirect('login')  # Redirect to login page after password reset email sent
    return render(request, 'reset_password.html')  # Show reset password form
