from rest_framework import serializers
from .models import Assignment, Student, Lecture, Course, User
from profiles.models import UserProfile
        
class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'phone_number' , 'age' , 'gender')

class UserRegistrationSerializer(serializers.ModelSerializer):
    profile = UserSerializer(required=False)

    class Meta:
        model = User
        fields = ('email','password','profile')
        extra_kwargs = {'password' : {'write_only': True }}

    def create(self,validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(
            user = user,
            first_name = profile_data['first_name'],
            last_name = profile_data['last_name'],
            phone_number = profile_data['phone_number'],
            age = profile_data['age'],
            gender = profile_data['gender']
        )
        return user 

