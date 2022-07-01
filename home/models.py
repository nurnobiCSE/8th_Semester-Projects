from django.db import models 

# Create your models here.

class Student(models.Model):
    st_id = models.CharField(max_length=20,blank=False)
    st_fname = models.CharField(max_length=200,blank=False)
    st_lname = models.CharField(max_length=200)
    address = models.TextField(max_length=500)
    gender =  models.CharField(max_length=200, blank=False)
    department = models.CharField(max_length=200)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.st_fname
 