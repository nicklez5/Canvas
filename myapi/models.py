from enum import auto
from time import time 
import jwt 
import uuid
from datetime import datetime, timedelta 

from django.db import models
from django.contrib.auth.models import ( AbstractBaseUser, BaseUserManager, PermissionsMixin  )
from django.conf import settings
from .managers import UserManager
from django.utils.translation import ugettext_lazy as _
def get_id():
    return int(time())


        
class User(AbstractBaseUser):
    username = models.CharField(db_index=True, max_length=255,unique=True)

    date_joined = models.DateTimeField(_('date joined'),auto_now_add = True)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email = models.EmailField(
        db_index=True,
        unique = True
    )
    user_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    #list_courses = models.ManyToManyField(Course,blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [''] 

    objects = UserManager()
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True 
    
    def has_module_perms(self, app_label):
        return True 

    @property
    def is_staff(self):
        return self.is_staff

    @property
    def is_superuser(self):
        return self.is_superuser

    class Meta:
        ordering = ['username']
        db_table = "login"
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = get_id()
            super(User,self).save(*args,**kwargs)
        return self 
        


# Create your models here.
