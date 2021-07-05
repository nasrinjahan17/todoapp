from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import *

from django.contrib.auth import authenticate,login,logout
from .forms import SignupForm,TodoForm
from django.contrib.auth.decorators import login_required


# function for indexpage.
def index(request):
    if request.user.is_authenticated:
        return redirect('todoapp:profile')
    else:
        return render(request,'index.html')

# function for signup.
def signup(request):
    if request.user.is_authenticated:
        return redirect('todoapp:profile')
    else:
        fm = SignupForm()
    if request.method == "POST":
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('todoapp:login')
    
    return render(request,'signup.html',{'fm':fm}) 

# function for login.
def user_login(request):
    msg = ''
    if request.user.is_authenticated:
        return redirect('todoapp:profile')
    else:
        if request.method == 'POST':
            username=request.POST.get("username")
            password=request.POST.get("password")
            user = authenticate(request, username=username, password=password)
                
            if user is not None: 
                login(request, user)
                return redirect('todoapp:profile')
            else:
                msg = 'Username or Password is incorrect'
                
    context = {'msg':msg}
    return render (request,'login.html',context)      
    
# Function for User-Profile
@login_required(login_url='todoapp:login')
def profile(request):
    if request.user.is_authenticated:
        form = TodoForm()
        return render(request,'profile.html', {'form':form})
    
def my_todos(request):
    if request.user.is_authenticated:
        user = request.user
    todos = To_Do.objects.filter(user=user).order_by('priority')
    return render(request,'my_todos.html',{'todos':todos})

# function for logout.
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


# This function is conected to profile function
def add_todo(request):
    if request.user.is_authenticated:
        user= request.user
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('todoapp:profile')
        else:
            return render(request,'profile.html',{'form':form})

# function for delete todo
def delete_todo(request,id):
    To_Do.objects.get(pk=id).delete()
    return redirect('todoapp:my_todos')

# function for change todo
def change_todo(request,id,status):
    change = To_Do.objects.get(pk=id)
    change.status = status
    change.save()
    return redirect('todoapp:my_todos')


# name = nasrin
# pass = #mitu123
