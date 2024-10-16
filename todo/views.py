from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "List": "/list/",
        "Detail View": "/detail/<int:id>",
        "Create": "/create/",
        "Update": "/update/<int:id>",
        "Delete": "/delete/<int:id>",
    }

    return Response(api_urls)


@api_view(["GET"])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def taskDetail(request, id):
    try:
        task = Task.objects.get(id=id)
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)
    
    except Task.DoesNotExist:
        return Response({"error": "Task not found."})


@api_view(["GET", "POST"])
def taskUpdate(request, id):
    task = Task.objects.get(id=id)
    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    return Response(serializer.errors, status=400)


@api_view(["POST"])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    data = request.data
    id = data.get("id")
    if Task.objects.filter(id=id).exists():
        return Response({"error": "A task with this ID already exists"}, status=400)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def taskDelete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return Response("Task is deleted")
