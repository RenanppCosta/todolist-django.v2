from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskModelForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required
def task_list(request):
    search = request.GET.get("search")
    filter = request.GET.get("filter")

    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)
    elif filter:
        if filter == "doing":
            tasks = Task.objects.filter(is_completed=False, user=request.user)
        elif filter == "done":
            tasks = Task.objects.filter(is_completed=True, user=request.user)
        else:
            tasks = Task.objects.filter(user=request.user)
    else:
        tasks_list = Task.objects.all().order_by("-created_at").filter(user=request.user)

        paginator = Paginator(tasks_list, 4)
        page = request.GET.get("page")

        tasks = paginator.get_page(page)

    return render(request, "tasks/list-tasks.html", {"tasks": tasks})

@login_required
def task_view(request, id):
    task = get_object_or_404(Task, id=id)

    return render(request, "tasks/task.html", {"task": task})

@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskModelForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("/tasks")
    else:
        form = TaskModelForm()

    return render(request,"tasks/create-task.html", {"form": form})

@login_required
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

@login_required   
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()

    messages.info(request, "Tarefa deletada com sucesso!")
    return redirect("/tasks")


@login_required

def complete_task(request, id):
    task = get_object_or_404(Task, id=id)

    task.is_completed = not task.is_completed
    task.save()

    return redirect("/tasks")