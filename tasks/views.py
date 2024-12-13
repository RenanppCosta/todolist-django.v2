from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskModelForm


def task_list(request):
    tasks = Task.objects.all().order_by("-created_at")

    return render(request, "tasks/list-tasks.html", {"tasks": tasks})

def task_view(request, id):
    task = get_object_or_404(Task, id=id)

    return render(request, "tasks/task.html", {"task": task})

def create_task(request):
    if request.method == "POST":
        form = TaskModelForm(request.POST)

        if form.is_valid():
            task = form.save()
            task.save()
            return redirect("/tasks")
    else:
        form = TaskModelForm()

    return render(request,"tasks/create-task.html", {"form": form} )