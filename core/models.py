from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserProfileManager(BaseUserManager):
    
    def create_user(self, email, name, password=None, **extra_fields):
        """Create and save a new user."""
        if not email:
            raise ValueError("Email isn't provided.")
        
        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        
        return user

    
    def create_superuser(self, email, name, password):
        """Create and save a new superuser."""
        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represent a user profile inside our system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get the full name of the user"""
        return self.name

    def __str__(self):
        return self.email

