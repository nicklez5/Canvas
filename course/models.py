import uuid
from django.db import models
from student.models import Student 
from lecture.models import Lecture
from assignment.models import Assignment
class Course(models.Model):
    name = models.CharField(max_length=40)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    lectures = models.ManyToManyField(Lecture)
    students = models.ManyToManyField(Student)
    assignments = models.ManyToManyField(Assignment)
    def __str__(self):
        return self.course_name

    class Meta:
        ordering = ['name']
        db_table = "Course"
# Create your models here.
