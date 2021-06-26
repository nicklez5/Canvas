from time import time 
import uuid 
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.conf import settings
from .managers import UserManager
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



class User(AbstractBaseUser):
    #username = models.CharField(max_length=30,unique=True)
    #password = models.CharField(max_length=100,editable=False,default='')
    #date_joined = models.DateTimeField(_('date joined'),auto_now_add = True)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email = models.EmailField(
        verbose_name = 'email address',
        max_length = 255,
        unique = True
    )
    #user_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    #list_courses = models.ManyToManyField(Course,blank=True)

    is_staff = models.BooleanField(_('staff status'),default=False,help_text=_('Determines if user can access the admin site'))
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 

    objects = UserManager()
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_staff
    
    def has_module_perms(self, app_label):
        return self.is_superuser

    class Meta:
        db_table = "login"
    
    #def save(self, *args, **kwargs):
        #if not self.user_id:
            #self.user_id = get_id()
        #super(User, self).save(*args, **kwargs)
        


# Create your models here.
