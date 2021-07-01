from rest_framework import serializers
from .models import Course 
class SerializeCourse(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'