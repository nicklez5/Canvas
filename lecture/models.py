from django.db import models
from django.utils.translation import ugettext_lazy as _ 
class Lecture(models.Model):
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(_('date created'),auto_now_add=True)
    name = models.CharField(max_length=100)
    imageFile = models.ImageField(upload_to='lectures')
    lecture_id = models.IntegerField(primary_key=True,editable=False)

    def save(self, *args, **kwargs):
        
# Create your models here.
