from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


class RegisterView(View):
    def post(self, request):
        first_name = request.POST.get('first_name' , "")
        last_name = request.POST.get('last_name' , "")
        username = request.POST.get('username' , "")
        password = request.POST.get('password', "")
        password1 = request.POST.get('password1', "")
        
        
        if password != password1:
            print("passwords do not match" , password , password1)
            return render(request, 'register.html', {'error': 'Passwords do not match'})
        
        try :
            User.objects.get(username=username)
            return render(request, 'register.html', {'error': 'Username already exists'})
        except :
            pass
        
        user = User.objects.create_user(first_name = first_name, last_name = last_name,username=username, password=password)
        user.save()
        login(request, user)
        return redirect('experiments_list')

    def get(self, request):
        return render(request, 'register.html')


class LoginView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('experiments_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    def get(self, request):
        return render(request, 'login.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('experiments_list')