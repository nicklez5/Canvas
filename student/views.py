from django.shortcuts import render, redirect
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import SerializeStudent
from rest_framework import status 
class StudentList(APIView):
    permission_classes = [AllowAny]
    def get(self,request,format=None):
        students = Student.objects.all()
        student_serializer = SerializeStudent(Student,many=True)
        return Response(student_serializer.data)

    def post(self,request,format=None):
        student_serializer = SerializeStudent(data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data, status=status.HTTP_201_CREATED)
        return Response(student_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

# Create your views here.
