from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Project, Task

# Create your views here.
def index(request):
    title = 'Django Course!!'
    return render(request, 'pagina.html', {
        'title': title
    })

def hello(request,id):
    return HttpResponse("<h1>Saludos</h1> <div>id:  %s</div>" % id)
    
def about(request):
    username= 'Josemi'
    return render(request, 'about.html', {
        'username': username
    })

def project(request):
    projects = list (Project.objects.values())
    return  JsonResponse(projects, safe=False)

def projecthtml(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {
        'projects' : projects
    })

def Tasks(request, id):
    try:
        task = Task.objects.values().get(id=id)
    except Task.DoesNotExist:
        return HttpResponse('Task not found', status=404)
    return JsonResponse(task)

def taskhtml(request):
    tasks = Task.objects.all()
    return render(request, 'task.html', {
        'tasks' : tasks
    })

def TasksperTitle(request, title):
    try:
        task = Task.objects.values().get(title=title)
    except Task.DoesNotExist:
        return HttpResponse('Task not found', status=404)
    return JsonResponse(task)