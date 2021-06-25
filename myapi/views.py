from django.shortcuts import render
from rest_framework import viewsets, status 
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .serializers import StudentSerializer, CourseSerializer, LectureSerializer, AssignmentSerializer, UserRegistrationSerializer
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

class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success' : 'True',
            'status code': status_code,
            'message': 'User registered successfully',
        }

        return Response(response,status=status_code)
        

# Create your views here.
