from time import time 
import uuid
from django.db import models
from course.models import Course 
from django.utils.translation import ugettext_lazy as _
def get_id():
    return int(time())
    
class Assignment(models.Model):
    course = models.ForeignKey('course.Course',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(null=True,blank=True)
    student_points = models.IntegerField(null=True,blank=True)
    max_points = models.IntegerField(null=True,blank=True)
    date_due = models.DateTimeField(_('date due'), auto_now_add = False)
    description = models.TextField(blank=True)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = get_id()
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_created']
        db_table = "assignment"
# Create your models here.
