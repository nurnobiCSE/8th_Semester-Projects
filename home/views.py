from django.shortcuts import render ,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# import all models
from .models import *
# Create your views here.
def faculty_log(request):
    return render(request,'faculty_login.html')

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

    return render(request, 'admin-dashboard.html')

@login_required
def student_add(request):
    
    if request.method == "POST":
        st_id = request.POST.get('st_id')
        st_fullname = request.POST.get('st_fname')
        gender = request.POST.get('st_gender')
        department = request.POST.get('st_department')
        semester = request.POST.get('st_semester')
        intake = request.POST.get('st_intake')
        section = request.POST.get('st_section')
        course = request.POST.get('st_course')
        if Student.objects.filter(st_id=st_id).exists():
            messages.warning(request,"This ID already exist try another ID !")
        else:    
            st_form = Student(
                st_id = st_id,
                st_fullname = st_fullname,
                gender = gender,
                department = department,
                semester = semester,
                intake = intake,
                section = section,
                course = course
            )

            st_form.save()
            messages.success(request, " Successfully Added New Student")
            return redirect('student')
    if 'q' in request.GET:
        q = request.GET['q']
        # student_data = Student.objects.filter(st_id__icontains=q)
        #for multiple query :
        multiple_q = Q(Q(st_id__icontains=q) | Q(st_fname__icontains=q) | Q(st_lname__icontains=q) |Q(address__icontains=q) | Q(department__icontains=q))
        student_data = Student.objects.filter(multiple_q)
    else:
        student_data = Student.objects.all()
                
    context = {
        'student_data' : student_data,
    }

    return render(request, 'student.html',context)

@login_required
def student_list(request):
    students = Student.objects.all()
    context={
        'students':students
    }
    return render(request, 'view_student_list.html',context)

@login_required
def addCourse_Faculty(request):
    if request.method =="POST":
        name = request.POST.get('course_name')
        dep = request.POST.get('department')
        semester = request.POST.get('semester')
        intake = request.POST.get('intake')
        section = request.POST.get('section')
        fac = request.POST.get('faculty')

        cours_form = CourseOfFaculty(
            course_name = name,
            department = dep,
            semester = semester,
            intake = intake,
            section = section,
            faculty = fac
        )
        cours_form.save()
    registeredCRS = CourseOfFaculty.objects.all()
    department = Department.objects.all()
    fac = Faculty.objects.all()
    context={
        'registerCours': registeredCRS,
        'department': department,
        'fac': fac
    }    
    return render(request, 'fac_reg_course.html', context)


@login_required
def student_edit(request,id):
    students = Student.objects.get(pk=id)
    context ={
        'students': students
    }
    return render(request,'edit.html',context)

@login_required
def update_student(request,id):
    students = Student.objects.get(pk=id)
    students.st_id = request.GET['st_id']
    students.st_fullname = request.GET['st_fname']
    students.gender = request.GET['st_gender']
    students.department = request.GET['st_department']
    students.semester = request.GET['st_semester']
    students.intake = request.GET['st_intake']
    students.section = request.GET['st_section']
    students.course = request.GET['st_course']
    

    students.save()
    messages.success(request,"Student Update Successfully!")
    return redirect('student')

@login_required
def delete_student(request,id):
    students = Student.objects.get(pk=id)
    students.delete()
    return redirect('student')

@login_required
def grades(request):

    return render(request, 'grades.html')

@login_required
def department(request):
    if request.method=="POST":
        code = request.POST.get('dep_code')
        name = request.POST.get('dep_name')

        dep_form = Department(
            dep_code = code,
            dep_name = name
        )
        dep_form.save()

    dep_data = Department.objects.all()
    context={
        'departments': dep_data
    }
    return render(request, 'department.html',context)

@login_required
def curriculum(request):
    if request.method == "POST":
        c_id = request.POST.get('c_id')
        code = request.POST.get('c_code')
        title = request.POST.get('c_title')
        department = request.POST.get('department')
        semester = request.POST.get('semester')
        credit = request.POST.get('c_credit')
        
        crc_form = Curriculum(
            course_id = c_id,
            course_code = code,
            course_title = title,
            department = department,
            semester = semester,
            credit = credit
        )
        crc_form.save()
    
    crc_data = Curriculum.objects.all()
    dep_data = Department.objects.all()
    context={
        'curriculums':crc_data,
        'departments':dep_data
    }


    return render(request, 'curriculum.html', context)

@login_required
def manageuser(request):
    if request.method == "POST":
        no = request.POST.get('f_no')
        code = request.POST.get('f_code')
        name = request.POST.get('f_fullname')
        username = request.POST.get('f_username')
        password = request.POST.get('f_password')

        fclt_form = Faculty(
            f_no = no,
            f_code = code,
            f_fullname = name,
            f_username = username,
            f_password = password

        )
        fclt_form.save()
    flt_data = Faculty.objects.all()
    context={
        'faculty':flt_data
    }    
         
    return render(request, 'manage-user.html', context)   

@login_required
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
