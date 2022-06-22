from django.urls import path
from .import views

urlpatterns = [
    
    path('register-user/',views.user_register,name='registration'),
    path('',views.dashboard,name='dashboard'),
    path('student-management/',views.student,name='student'),
    path('grades-management/',views.grades,name='grades'),
    path('department-management/',views.department,name='department'),
    path('curriculum-management/',views.curriculum,name='curriculum'),
    path('user-management/',views.manageuser,name='manageuser'),
    path('prerequisite-management/',views.prerequisite,name='prerequisite'),
     
]