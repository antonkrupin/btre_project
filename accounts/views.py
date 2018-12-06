from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password2 = request.POST['password2']
        password = request.POST['password']

        # Check if passwords match

        if password == password2:
            # Check user name
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Это имя уже занято')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Эта электронная почта уже используется')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password,
                                                    email=email, first_name=first_name,
                                                    last_name=last_name)
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'Теперь вы авторизованы')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'Теперь вы зарегистрированы и можете войти под своим логином и паролем')
                    return redirect('login')
        else:
            messages.error(request, 'Пароли не совпадают')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Добро пожаловать')
            return redirect('dashboard')
        else:
            messages.error(request, 'Не правильный логин или пароль')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Вы успешно вышли из личного кабинета')
        return redirect('index')


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)
