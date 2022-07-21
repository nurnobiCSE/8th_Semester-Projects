from django.urls import path
from .import views

urlpatterns = [
    
    path('register-user/',views.user_register,name='registration'),
    path('faculty-user-login/',views.faculty_log,name='faculty_log'),
    path('',views.dashboard,name='dashboard'),
    path('student-management/',views.student_add,name='student'),
    path('student-list/',views.student_list,name='student_list'),
    path('student_edit/<id>/',views.student_edit,name='student_edit'),
    path('update_student/<id>/',views.update_student,name='update_student'),
    path('delete_student/<id>/',views.delete_student,name='delete_student'),
    path('grades-management/',views.grades,name='grades'),
    path('department-management/',views.department,name='department'),
    path('curriculum-management/',views.curriculum,name='curriculum'),
    path('user-management/',views.manageuser,name='manageuser'),
    path('prerequisite-management/',views.prerequisite,name='prerequisite'),
    path('addCourse-to-Faculty/',views.addCourse_Faculty,name='addCourse_Faculty'),
     
]