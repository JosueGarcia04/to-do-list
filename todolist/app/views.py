from django.shortcuts import render
from .models import Task
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    database = Task.objects.all()
    context = {
        "database": database
    }

    return render(request, "app/index.html", context)

def insert(request):
    task_subject = request.POST["subject"]
    task_description = request.POST["description"]
    database = Task(subject=task_subject, description=task_description)
    database.save()
    return HttpResponseRedirect(reverse("index"))
