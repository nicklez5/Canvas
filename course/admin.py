from django.contrib import admin
from .models import Lecture, Course, Student, Assignment 
admin.site.register(Assignment)
admin.site.register(Student)
admin.site.register(Lecture)
admin.site.register(Course)

# Register your models here.
