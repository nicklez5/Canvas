
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email address')
        
        user = self.model(
            username = username,
            email = self.normalize_email(email),
        )
        user.set_password(password)
        
        user.save()

        return user
    
    def create_superuser(self,username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active', True)

        if password is None:
            raise TypeError('Staff must have a password.')
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            username,
            email,
            password,
            **extra_fields
        )
        
        user.save()
        return user
        
        