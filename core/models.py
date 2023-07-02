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
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManger()
    USERNAME_FIELD = 'email'

class UserDocumentUpload(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    dr_name = models.CharField(max_length=30)
    prescription = models.ImageField(upload_to='documents/image/')
    report = models.FileField(upload_to='documents/pdfs/')

    def __str__(self):
        return self.name