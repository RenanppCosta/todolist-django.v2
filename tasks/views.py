from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskModelForm
from django.contrib import messages
from django.core.paginator import Paginator


def task_list(request):
    tasks_list = Task.objects.all().order_by("-created_at")

    paginator = Paginator(tasks_list, 4)
    page = request.GET.get("page")

    tasks = paginator.get_page(page)

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

    return render(request,"tasks/create-task.html", {"form": form})

def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    form = TaskModelForm(instance=task)

    if request.method == "POST":
        form = TaskModelForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            task.save()
            return redirect("/tasks")
        else:
            return render(request,"tasks/update-task.html", {"form": form, "task": task})
    else:
        return render(request,"tasks/update-task.html", {"form": form, "task": task})
    
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()

    messages.info(request, "Tarefa deletada com sucesso!")
    return redirect("/tasks")