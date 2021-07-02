from time import time 
import uuid 
from django.db import models
from course.models import Course 
from django.utils.translation import ugettext_lazy as _ 
def get_id():
    return int(time())
class Lecture(models.Model):
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(_('date created'),auto_now_add=True)
    name = models.CharField(max_length=100)
    imageFile = models.ImageField(upload_to='lectures')
    id = models.IntegerField(primary_key=True,editable=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = get_id()
        super().save(*args, **kwargs)
         
    class Meta:
        ordering = ['name']
        db_table = "lecture"

# Create your models here.
