from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Assignment
from .serializers import SerializeAssignment
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status 

class AssignmentList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        assignments = Assignment.objects.all()
        serializer = SerializeAssignment(assignments, many=True)
        return Response(serializer.data)

class AssignmentPost(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request, format=None):
        serializer = SerializeAssignment(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignmentDetail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Assignment.objects.get(pk=pk)
        except Assignment.DoesNotExist:
            raise Http404

    def get(self, request, pk , format=None):
        assignment = self.get_object(pk)
        serializer = SerializeAssignment(assignment)
        return Response(serializer.data)

class AssignmentUpdate(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]

    def put(self, request, pk, format=None):
        assignment = self.get_object(pk)
        serializer = SerializeAssignment(assignment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AssignmentDelete(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]

    def delete(self, request, pk, format=None):
        assignment = self.get_object(pk)
        assignment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Create your views here.

# Create your views here.
