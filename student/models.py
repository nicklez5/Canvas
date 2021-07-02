from time import time 
import uuid
from assignment.models import Assignment
from profiles.models import UserProfile
from django.db import models
def get_id():
    return int(time())

class Student(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    profile = models.ForeignKey("profile.Profile",blank=True)
    name = models.CharField(default='"%s" % profile')
    list_assignments = models.ManyToManyField("assignment.Assignment",related_name="assignments", blank=True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = get_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return "%s" % (self.profile)
# Create your models here.
