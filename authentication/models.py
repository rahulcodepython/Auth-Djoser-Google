from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from . import manager as self_manager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=254)
    first_name = models.CharField(max_length=1000, blank=True)
    last_name = models.CharField(max_length=1000, blank=True)
    age = models.IntegerField(default=0)
    bio = models.TextField(blank=True)
    # password .....

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    groups = None
    user_permissions = None
    last_login = None
    
    objects = self_manager.UserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name']

    USERNAME_FIELD = 'email' 

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'
        ordering = ['email']

    def __str__(self) -> str :
        return self.email  
