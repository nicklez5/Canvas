import uuid
from profiles.models import UserProfile
from django.db import models
class Student(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    profile = models.ForeignKey(UserProfile)
    student_name = profile.__str__()
    
    def __str__(self):
        return self.student_name 
# Create your models here.
