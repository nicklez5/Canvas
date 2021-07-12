from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from rest_framework import viewsets, status 
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView 
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .serializers import RegistrationSerializer

class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    
    def post(self,request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
# #
# class UserRegistrationView(CreateAPIView):
#     serializer_class = UserRegistrationSerializer
#     permission_classes = (AllowAny,)

#     def post(self,request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         status_code = status.HTTP_201_CREATED
#         response = {
#             'success' : 'True',
#             'status code': status_code,
#             'message': 'User registered successfully',
#         }

#         return Response(response,status=status_code)

# class UserLoginView(APIView):
#     permission_classes = (AllowAny,)
#     serializer_class = UserLoginSerializer

#     def post(self,request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         response = {
#             'success' : 'True',
#             'status code': status.HTTP_200_OK,
#             'message' : 'User logged in successfully',
#             'token' : serializer.data['token'],
#         }
#         status_code = status.HTTP_200_OK

#         return Response(response,status=status_code)


# class UserListView(APIView):
#     permission_classes = (AllowAny,)
#     def get(self,request,format=None):
#         users = User.objects.all()
#         serializer = UserListSerializer(users,many=True)
#         return Response(serializer.data)
# q
#     def post(self,request, format=None):
#         serializer = UserListSerializer(data=request.data)
        

