from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
     def create_user(self, email, first_name, last_name, password=None, **other_fields):
        """creates and saves a user with a given email and password"""

        if not email:
            raise ValueError('user must have the email address')
        user= self.model(email=self.normalize_email(email), first_name=first_name,
                          last_name=last_name, **other_fields)
        user=user.set_password(password)
        user=user.save(using=self._db)
        return user

     def create_superUser(self, email, first_name, last_name, password, **other_fields):
        """Create and save a new superuser"""
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True')
        return self.create_user(email, first_name, last_name, password, **other_fields)

class CustomUser(AbstractBaseUser):
    """Custom user model that support using email instead of username"""
    USER_TYPE=[['S','staff'],
                ['U','Normal User'],
    ]
    user_id=models.IntegerField(max_length=6,null=False,unique=False)           
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    userType =  models.CharField( max_length=100,choices=USER_TYPE,blank=False, null=False)
    telephone = models.CharField(max_length=20, blank=False, null=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)


    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name()        
        