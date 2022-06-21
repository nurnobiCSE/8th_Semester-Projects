from django.shortcuts import render ,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print("username does not exist")    
        user = authenticate(request, username=username, password=password)    
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            print("username or password is incorrect !")    
    return render(request,"index.html")

def dashboard(request):

    return render(request, 'faculty-dashboard.html')

def student(request):

    return render(request, 'student.html')

def grades(request):

    return render(request, 'grades.html')

def department(request):

    return render(request, 'department.html')


def curriculum(request):

    return render(request, 'curriculum.html')

def manageuser(request):

    return render(request, 'manage-user.html')   

def prerequisite(request):

    return render(request, 'pre-requisite.html')     

def user_register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        fcode = request.POST['fcode']
        department = request.POST['department']
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.warning(request,"This email already exist try another email !")
        else:
            user = User.objects.create_user(username=username,password=password,first_name=fname)
            user.save()
            messages.success(request,"New Faculty added!!")    
            return redirect('login')    

    return render(request,'faculty-reg.html')
