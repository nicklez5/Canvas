from enum import auto
from time import time 
import jwt 
import uuid
from datetime import datetime, timedelta 

from django.db import models
from django.contrib.auth.models import ( AbstractBaseUser, BaseUserManager, PermissionsMixin,  )
from django.conf import settings
from .managers import UserManager
from django.utils.translation import ugettext_lazy as _
def get_id():
    return int(time())



class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email address')
        
        user = self.model(
            username = username,
            email = self.normalize_email(email)
        )
        user.set_password(password)
        
        user.save()

        return user
    
    def create_superuser(self,username, email, password):
        

        if password is None:
            raise TypeError('Superuser must have a password.')
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            username,
            email,
            password
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
        
        
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255,unique=True)
    #password = models.CharField(max_length=100,editable=False,default='')
    #date_joined = models.DateTimeField(_('date joined'),auto_now_add = True)
    #id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email = models.EmailField(
        db_index=True,
        unique = True
    )
    #user_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    #list_courses = models.ManyToManyField(Course,blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    #is_superuser = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] 

    objects = UserManager()
    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.username
    
    def get_short_name(self):
        return self.username
    
    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)
        token = jwt.encode({
            'id': self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')
        
    # def has_perm(self, perm, obj=None):
    #     return True 
    
    # def has_module_perms(self, app_label):
    #     return True 

    # @property
    # def is_staff(self):
    #     return self.is_staff

    # @property
    # def is_superuser(self):
    #     return self.is_superuser

    # class Meta:
    #     ordering = ['email']
    #     db_table = "login"
    
    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.id = get_id()
    #         super(User,self).save(*args,**kwargs)
    #     return self 
        


# Create your models here.
