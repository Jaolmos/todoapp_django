from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def home(request):
    # Vista de la pagina de inicio
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'todo/home.html', context)


def add_task(request):
    # Vista para agregar una nueva tarea
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = TaskForm()

    context = {'form': form}
    return render(request, 'todo/add.html', context)


def edit_task(request, task_id):
    # Vista para editar una tarea
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)

    context = {'form': form}
    return render(request, 'todo/edit.html', context)


def delete_task(request, task_id):
    # Vista para eliminar una tarea
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')
