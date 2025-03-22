from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.views import APIView

from sharing_hub.models import Upload
from sharing_hub.serializers import UploadSerializer


# Create your views here.
def index(request):
    return render(request, "sharing_hub/index.html")


def upload(request):
    if request.method == "POST":
        file = request.FILES["file"]
        Upload.objects.create(user=request.user, file=file)
        return render(
            request,
            "sharing_hub/upload.html",
            {"message": "File uploaded successfully"},
        )
    return render(request, "sharing_hub/upload.html")


def dashboard(request):
    uploads = Upload.objects.filter(user=request.user)
    return render(request, "sharing_hub/dashboard.html", {"uploads": uploads})


def delete_item(request, slug):
    Upload.objects.filter(slug=slug).delete()
    return redirect("dashboard")


class UploadView(APIView):
    def get(self, request, slugs=None):
        if slugs:
            slug_list = slugs.split(",")  # Splitting slugs correctly
            uploads = Upload.objects.filter(slug__in=slug_list)
        else:
            uploads = Upload.objects.all()  # Ensure uploads is always defined

        serializer = UploadSerializer(uploads, many=True)
        return Response(
            {
                "uploads": serializer.data,
            }
        )


def shared_page(request, slugs):
    slug_list = slugs.split(",")
    shared_files = Upload.objects.filter(slug__in=slug_list)
    return render(request, "sharing_hub/shared_page.html", {"shared_files": shared_files})