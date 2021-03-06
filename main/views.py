from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.
def index(request):
    projects = Project.objects.all().order_by("-project_published")
    image_urls = [p.project_image.url.split("main/static/")[1] for p in projects]
    projects = zip(projects, image_urls)
    return render(request,
                  "main/home.html",
                {"projects": projects})

def about(request):
    return render(request,
            "main/about.html")