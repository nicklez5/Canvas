from time import time 
import uuid 
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
from .managers import UserManager
from django.utils.translation import ugettext_lazy as _
def get_id():
    return int(time())


class User(AbstractBaseUser):
    #username = models.CharField(max_length=30,unique=True)
    #password = models.CharField(max_length=100,editable=False,default='')
    #date_joined = models.DateTimeField(_('date joined'),auto_now_add = True)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email = models.EmailField(
        verbose_name = 'email address',
        max_length = 255,
        unique = True
    )
    #user_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    #list_courses = models.ManyToManyField(Course,blank=True)

    is_staff = models.BooleanField(_('staff status'),default=False,help_text=_('Determines if user can access the admin site'))
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 

    objects = UserManager()
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_staff
    
    def has_module_perms(self, app_label):
        return self.is_superuser

    class Meta:
        ordering = ['email']
        db_table = "login"
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = get_id()
        super(User, self).save(*args, **kwargs)
        


# Create your models here.
