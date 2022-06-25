from django.shortcuts import render ,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# import all models
from .models import *
# Create your views here.
@login_required
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


@login_required
def dashboard(request):

    return render(request, 'faculty-dashboard.html')

@login_required
def student_add(request):
    
    if request.method == "POST":
        st_id = request.POST.get('st_id')
        st_fname = request.POST.get('st_fname')
        st_lname = request.POST.get('st_lname')
        address = request.POST.get('st_address')
        gender = request.POST.get('st_gender')
        department = request.POST.get('st_department')
        course = request.POST.get('st_course')
        st_form = Student(
            st_id = st_id,
            st_fname = st_fname,
            st_lname = st_lname,
            address = address,
            gender = gender,
            department = department,
            course = course
        )

        st_form.save()
        messages.success(request, " Successfully Added New Student")
        return redirect('student')
    if 'q' in request.GET:
        q = request.GET['q']
        # student_data = Student.objects.filter(st_id__icontains=q)
        #for multiple query :
        multiple_q = Q(Q(st_id__icontains=q) | Q(st_fname__icontains=q) | Q(st_lname__icontains=q) |Q(address__icontains=q) | Q(department__icontains=q)|Q(course__icontains=q))
        student_data = Student.objects.filter(multiple_q)
    else:
        student_data = Student.objects.all()
                
    context = {
        'student_data' : student_data,
    }

    return render(request, 'student.html',context)

@login_required
def grades(request):

    return render(request, 'grades.html')

@login_required
def department(request):

    return render(request, 'department.html')

@login_required
def curriculum(request):

    return render(request, 'curriculum.html')

@login_required
def manageuser(request):

    return render(request, 'manage-user.html')   

@login_required
def prerequisite(request):

    return render(request, 'pre-requisite.html')     

@login_required
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
