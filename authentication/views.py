from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.shortcuts import redirect, render

from authentication.forms import UserForm


# Create your views here.
def sign_in(request):
    form = UserForm()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if not user:
            return Http404("Invalid Credentials")
        login(request, user)
        return redirect("dashboard")
    return render(request, "authentication/login.html", {"form": form})


def sign_up(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = UserForm()
    return render(request, "authentication/signup.html", {"form": form})

def edit_profile(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pro_pic=request.FILES['pro_pic']
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.pro_pic = pro_pic
        user.save()
        return redirect('profile')
    return render(request, "authentication/profile.html")

def sign_out(request):
    logout(request)
    return redirect("index")


def profile(request):
    return render(request, "authentication/profile.html")
