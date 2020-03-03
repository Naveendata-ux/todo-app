from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required

def index(request):
    
    todo_list=Todo.objects.order_by('id').filter(user_id=request.user.id)
    form =TodoForm()

    context={
        'todo_list':todo_list,
        'form':form
    }
    return render(request,'todo/index.html',context)


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo=Todo(text=request.POST['text'],user_id=request.user.id)
        new_todo.save()
        return redirect('todo:index')

def completedTodo(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.completed=True
    todo.save()
    return redirect('todo:index')

def deleteCompletedTodo(request):
    Todo.objects.all().filter(completed=True,user_id=request.user.id).delete()
    return redirect('todo:index')

def deleteAll(request):
    Todo.objects.all().filter(user_id=request.user.id).delete()
    return redirect('todo:index')



