from django.shortcuts import render
from .models import Task
from django.http import HttpResponse

# Create your views here.
def index(request):
    database = Task.objects.all()
    context = {
        "database": database
    }
    print(database)
    return render(request, "app/index.html", context)

def insert(request):
    return HttpResponse("hi django")