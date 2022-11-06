from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def login(requst):
    if requst.method == 'POST':
        username = requst.POST['username']
        password = requst.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(requst, user)
            return redirect("/")
        else:
            messages.info(requst, 'Invalid Username or Password. Try again')
            return redirect('login')
        
    else:
        return render(requst, 'login.html')

# Create your views here.
def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                # print("Username Taken")
                print('\U0001F600')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                # print("Email already exists")
                print('\U0001F600')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                messages.info(request, 'User Saved')
                # print('User Saved')
                print('\U0001F600')
                return redirect('login')
        else:
            messages.info(request, 'Passwords not matching')
            # print("Passwords not matching")
            return redirect('register')

    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')