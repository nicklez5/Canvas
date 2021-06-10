from time import time 
from django.db import models
from django.utils.translation import ugettext_lazy as _

def get_id():
    return int(time())

class Assignment(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(_('date created'),auto_now_add = True)
    max_points = models.IntegerField(null=True,blank=True)
    user_point = models.IntegerField(null=True,blank=True)
    date_due = models.DateTimeField(_('date due'), auto_now_add = False)
    description = models.TextField(blank=True)
    assignment_id = models.IntegerField(primary_key=True,editable=False)

    def save(self, *args, **kwargs):
        if not self.assignment_id:
            self.assignment_id = get_id()
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    list_assignments = models.ManyToManyField(Assignment,blank=True)
    student_id = models.IntegerField(primary_key=True,editable=False)

    def save(self, *args, **kwargs):
        if not self.student_id:
            self.student_id = get_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Lecture(models.Model):
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(_('date created'),auto_now_add=True)
    name = models.CharField(max_length=50)
    imageFile = models.ImageField(upload_to='lectures')
    lecture_id = models.IntegerField(primary_key=True,editable=False)

    def save(self, *args, **kwargs):
        if not self.lecture_id:
            self.lecture_id = get_id()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Course(models.Model):
    list_students = models.ManyToManyField(Student,blank=True)
    list_lectures = models.ManyToManyField(Lecture,blank=True)
    name = models.CharField(max_length=50)
    course_id = models.IntegerField(primary_key=True,editable=False)

    def save(self, *args, **kwargs):
        if not self.course_id:
            self.course_id = get_id()
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name

# Create your models here.
