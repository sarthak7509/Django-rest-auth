from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.conf import settings

# Create your models here.

class UserManger(BaseUserManager):
    '''Mange Users'''
    def create_user(self,email,password=None,**kwargs):
        if not email:
            raise ValueError('User must have email')
        user = self.model(email=self.normalize_email(email),**kwargs)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password):
        user = self.create_user(email,password)
        user.is_staff=True
        user.is_superuser=True
        user.save()
        return user
class User(AbstractBaseUser,PermissionsMixin):
    '''user model in system'''
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManger()
    USERNAME_FIELD = 'email'