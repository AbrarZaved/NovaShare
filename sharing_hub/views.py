from django.shortcuts import render

from sharing_hub.models import Share


# Create your views here.
def index(request):
    return render(request, "sharing_hub/index.html")


def upload(request):
    if request.method == "POST":
        file = request.FILES["file"]
        Share.objects.create(user=request.user, file=file)
        return render(
            request,
            "sharing_hub/upload.html",
            {"message": "File uploaded successfully"},
        )
    return render(request, "sharing_hub/upload.html")


def dashboard(request):
    uploads = Share.objects.filter(user=request.user)
    return render(request, "sharing_hub/dashboard.html", {"uploads": uploads})
