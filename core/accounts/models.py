from django.db import models

from django.db import models
from django.contrib.auth.models import(BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
 

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication insted of the usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save user with the given email and password and extra data.
        """
        if not email:
            raise ValueError(_("The email must be set"))
        email = self.normalize_email(email)
        user =  self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
        

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save superuser with the given email and password and extra data.
        """
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))
        
        return self.create_user(email,password,**extra_fields)
    


class User(AbstractBaseUser,PermissionsMixin):
    """
    Custom User Model for our app
    """

    email = models.EmailField(max_length=250,unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_verified = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    
    def __str__(self):
        return self.email
    

