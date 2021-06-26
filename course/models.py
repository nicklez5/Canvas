import uuid
from django.db import models
from student.models import Student 
class Course(models.Model):
    course_name = models.CharField(max_length=40)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.course_name
# Create your models here.
