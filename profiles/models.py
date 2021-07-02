from time import time 
import uuid
from django.db import models
from myapi.models import User
def get_id():
    return int(time())

class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    first_name = models.CharField(max_length=50,unique=False)
    last_name = models.CharField(max_length=50,unique=False)
    phone_number = models.CharField(max_length=10,unique=True,null=False,blank=False)
    age = models.PositiveIntegerField(null=False,blank=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = get_id()
        super().save(*args,**kwargs)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = "profile"
    
    