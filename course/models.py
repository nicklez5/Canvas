from time import time
import uuid
from django.db import models
from student.models import Student 
from lecture.models import Lecture
from assignment.models import Assignment
def get_id():
    return int(time())
class Course(models.Model):
    name = models.CharField(max_length=40)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    lectures = models.ManyToManyField(Lecture,blank=True)
    students = models.ManyToManyField(Student,blank=True)
    assignments = models.ManyToManyField(Assignment,blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = get_id()
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = "course"
# Create your models here.
