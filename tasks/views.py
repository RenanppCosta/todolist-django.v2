from django.shortcuts import render, get_object_or_404
from .models import Task


def task_list(request):
    tasks = Task.objects.all()

    return render(request, "tasks/list-tasks.html", {"tasks": tasks})

def task_view(request, id):
    task = get_object_or_404(Task, id=id)

    return render(request, "tasks/task.html", {"task": task})