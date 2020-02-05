from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, \
                                        PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """create and save user"""
        if not email:
            raise ValueError('You must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_super_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('You must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractUser, PermissionsMixin):
    """customize user model"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

    REQUIRED_FIELDS = ['name']
    USERNAME_FIELD = 'email'
