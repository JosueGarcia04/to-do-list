from django.shortcuts import render, get_object_or_404
from .models import Task
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages

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
        messages.success(request, "Tarea añadida")
        return HttpResponseRedirect(reverse("index"))
    except ValueError as err:
        messages.error(request, str(err))
        return HttpResponseRedirect(reverse("index"))

def update_form(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task_subject = request.POST.get("subject")
        task_description = request.POST.get("description")
        if task_subject == "" or task_description == "":
            messages.error(request, "El texto no puede estar vacío :(")
        else:
            task.subject = task_subject
            task.description = task_description
            task.save()
            messages.success(request, "Tarea actualizada con éxito")
            return HttpResponseRedirect(reverse("index"))
    context = {
        "task": task
    }
    return render(request, "app/update.html", context)

def delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    messages.success(request, "Tarea borrada con éxito.")
    return HttpResponseRedirect(reverse("index"))


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username == "josue123" and password == "josue123":
            return redirect("index")
        else:
            messages.error(request, "Credenciales inválidas")
            return redirect("login")
    return render(request, "app/login.html")


def logout(request):
    messages.info(request, "Haz cerrado sesion ¿ingresar de nuevo?")
    return render(request, "app/logout.html")