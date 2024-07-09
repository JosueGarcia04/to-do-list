from django.shortcuts import render, get_object_or_404
from .models import Task
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    database = Task.objects.all()
    context = {
        "database": database[::-1]
    }
    return render(request, "app/index.html", context)

def insert(request):
    try:
        task_subject = request.POST["subject"]
        task_description = request.POST["description"]
        if task_subject == "" or task_description == "":
            raise ValueError("El texto no puede estar vacío :(")
        database = Task(subject=task_subject, description=task_description)
        database.save()
        return HttpResponseRedirect(reverse("index"))
    except ValueError as err:
        print(err)
        return HttpResponseRedirect(reverse("index"))

def delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return HttpResponseRedirect(reverse("index"))
