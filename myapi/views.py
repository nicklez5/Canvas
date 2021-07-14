from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from rest_framework import viewsets, status 
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from .serializers import (LoginSerializer, RegistrationSerializer, UserSerializer)
from .renderers import UserJSONRenderer

class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer
    
    def post(self,request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # Notice here that we do not call `serializer.save()` like we did for
        # the registration endpoint. This is because we don't  have
        # anything to save. Instead, the `validate` method on our serializer
        # handles everything we need.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        # There is nothing to validate or save here. Instead, we just want the
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        # Here is that serialize, validate, save pattern we talked about
        # before.
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


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
        

