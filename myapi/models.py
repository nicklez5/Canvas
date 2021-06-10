from django.db import models
from .managers import UserManager
from django.utils.translation import ugettext_lazy as _
class Profile(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100,editable=False,default='')
    date_joined = models.DateTimeField(_('date joined'),auto_now_add = True)
    is_staff = models.BooleanField(_('staff status'), default=False,help_text=_('Determines if user can access the admin site'))
    email = models.EmailField(_('email address'),unique=True)
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'is_staff']
    
    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_staff
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        
# Create your models here.
