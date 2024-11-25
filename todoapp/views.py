from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'templates/index.html', {'tasks': tasks, 'form': form})

def delete_task(request,task_id):
    task = Task.objects.get(id = task_id)
    task.delete()
    return redirect('/')


