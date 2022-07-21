from django.db import models 

# Create your models here.

class Student(models.Model):
    st_id = models.CharField(max_length=20,blank=False,default="")
    st_fullname = models.CharField(max_length=200,blank=False,default="")
    gender =  models.CharField(max_length=200, blank=False,default="")
    department = models.CharField(max_length=200,default="")
    semester = models.CharField(max_length=200,default="")
    intake = models.CharField(max_length=200,default="")
    section = models.CharField(max_length=200,default="")
    course = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.st_fname

class Department(models.Model):
    dep_code = models.CharField(max_length=10)
    dep_name = models.CharField(max_length=20)

    def __str__(self):
        return self.dep_name

class Curriculum(models.Model):
    course_id = models.CharField(max_length=10)
    course_code = models.CharField(max_length=10)
    course_title = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    semester = models.CharField(max_length=14)
    credit = models.CharField(max_length=10)

    def __str__(self):
        return self.course_code


class Faculty(models.Model):
    f_no = models.CharField(max_length=10)
    f_code = models.CharField(max_length=10)
    f_fullname = models.CharField(max_length=100)
    f_username = models.CharField(max_length=100)
    f_password = models.CharField(max_length=100)

    def __str__(self):
        return self.f_code

class CourseOfFaculty(models.Model):
    course_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    intake = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)