from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        password2 = request.POST['password2']

        #check if passwords match
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'this username already taken')
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'this email already taken')
                    return redirect('accounts:register')
                else:
                    #every thing valid
                    user =User.objects.create_user(username=username,email=email,first_name=first_name,
                                                last_name=last_name,password=password)
                    user.save()
                    messages.success(request,'you are now registered and can login ') 
                    return redirect('accounts:login')
        else:
            messages.error(request,'password does not matched ') 
            return redirect('accounts:register')
    else:
        return render(request,'accounts/register.html')



def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.error(request,'you are now logged in') 
            return redirect('todo:index')
        else:
            messages.error(request,'invalid username or password') 
            return redirect('accounts:login')

    return render(request,'accounts/login.html')

