from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo,TodoTasks
from .forms import todoForm,todoTaskForm,UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required(login_url="signin")
def home(request):  
    user = request.user
    message ="""Welcome to """ + user.username + """'s Todo list""" 
    todos = Todo.objects.filter(user = user)
    context = {
        'message' :message,
        'todos':todos,
        "user": user,
    }
    return  render(request , 'home.html' , context)

def singleTask(request , id):
    todo = Todo.objects.get(id = id)
    tasks = todo.todotasks_set.all()
    context={
        "todo": todo,
        "tasks" :tasks
    }
    return render(request , 'cruds/singleTask.html' , context)

@login_required(login_url="signin")
def createTodo(request):
    form = todoForm()
    user = request.user
    if request.method == "POST":
        form = todoForm(request.POST)
        if form.is_valid():
            user_todo = form.save(commit=False)
            user_todo.user = user
            user_todo.save()
            return redirect('/')
    context = {
        "form": form
    }
    return render(request , 'cruds/create.html' , context)

def updateTask(request , id):
    todo = Todo.objects.get(id = id)
    form = todoForm(instance=todo)
    if request.method == "POST":
        form = todoForm(request.POST , instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form
    }
    return render(request , 'cruds/update.html' , context)

def deleteTask(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')

def createItem(request,id):
    form = todoTaskForm()
    myTodo = Todo.objects.get(id = id)
    if request.method == "POST":
        form = todoTaskForm(request.POST)
        if form.is_valid():
            todo_task = form.save(commit=False)
            todo_task.task = myTodo
            todo_task.save()
            return redirect('/')
    context = {
        "form": form
    }
    return render(request , 'cruds/createItem.html' , context)

def updateItem(request , id):
    task = TodoTasks.objects.get(id = id)
    form = todoTaskForm(instance=task)
    if request.method == "POST":
        form = todoForm(request.POST , instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form
    }
    return render(request , 'cruds/updateItem.html' , context)

def deleteItem(request,id):
    task = TodoTasks.objects.get(id=id)
    task.delete()
    return redirect('/')

def signup(req):
    form = UserCreationForm()
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save() 
        else:
            print (form.errors)
        return redirect('/')
    context = {
        "form": form
    }
    return render(req, "signup.html", context)

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            errorMsg = """Invalid username or password"""
            context = {
                "errorMsg":errorMsg
            }
            return render(request , 'signin.html' , context)
            return redirect('/',context)

    return render(request, "signin.html")

def signout(request):
    logout(request)
    return redirect('/')
    