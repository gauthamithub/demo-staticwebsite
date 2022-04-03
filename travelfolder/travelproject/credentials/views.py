from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
            username = request.POST['username']
            firstname = request.POST['first_name']
            lastname = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            confirmpassword = request.POST['confirm_password']
            if password == confirmpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already exist')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Email already exist')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                    user.save()
                    return redirect('login')
            else:
                messages.info(request,'Password not match')
            return redirect('register')
    return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials !!')
            return redirect('login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')