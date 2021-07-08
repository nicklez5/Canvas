from time import time
import uuid
from django.db import models

def get_id():
    return int(time())
class Course(models.Model):
    name = models.CharField(max_length=40)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    lectures = models.ManyToManyField('lecture.Lecture',blank=True)
    students = models.ManyToManyField('student.Student',blank=True)
    assignments = models.ManyToManyField('assignment.Assignment',blank=True)

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
