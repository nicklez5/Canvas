import uuid 
from django.db import models
from course.models import Course 
from django.utils.translation import ugettext_lazy as _ 
class Lecture(models.Model):
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(_('date created'),auto_now_add=True)
    name = models.CharField(max_length=100)
    imageFile = models.ImageField(upload_to='lectures')
    id = models.IntegerField(primary_key=True,editable=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
         
    class Meta:
        ordering = ['name']
        db_table = "lecture"

# Create your models here.
