from django.contrib.auth import authenticate,login,logout
from django.http import Http404
from django.shortcuts import redirect, render


# Create your views here.
def sign_in(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if not user:
            return Http404("Invalid Credentials")
        login(request, user)
        return redirect('dashboard')
    return render(request, "authentication/login.html")

def sign_out(request):
    logout(request)
    return redirect('index')

def profile(request):
    return render(request, 'authentication/profile.html')