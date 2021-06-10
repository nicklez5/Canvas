from django.shortcuts import render
from rest_framework import viewsets

from .serializers import StudentSerializer, CourseSerializer, LectureSerializer, AssignmentSerializer
from .models import Assignment, Student, Lecture, Course
class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all().order_by('name')
    serializer_class = AssignmentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('name')
    serializer_class = StudentSerializer

class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all().order_by('name')
    serializer_class = LectureSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('name')
    serializer_class = CourseSerializer
    

# Create your views here.
