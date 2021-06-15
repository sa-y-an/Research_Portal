from django.db import models
from user import constants

# Create your models here.


class Faculty(models.Model):
    college_email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    




class Student(models.Model):
    college_email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    reg_no= models.CharField(max_length=20)
    program= models.CharField(max_length=20, choices=constants.STUDENT_PROGRAMS)
    graduation_year= models.IntegerField()


    
    

