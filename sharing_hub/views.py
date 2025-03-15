from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'sharing_hub/index.html')
def upload(request):
    return render(request, 'sharing_hub/upload.html')
def login(request):
    return render(request, 'sharing_hub/login.html')
def dashboard(request):
    return render(request, 'sharing_hub/dashboard.html')