from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,Permission,Group

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.FloatField()
    acitve = models.BooleanField()
    added = models.DateTimeField(default=now)
    def __str__(self) -> str:
        return self.name

class Users(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    created = models.DateTimeField(default=now)
    groups = models.ManyToManyField(Group, related_name='user_profiles')
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_profiles',
        blank=True,
    )
    # Required for Django authentication system
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.username

class Orders(models.Model):
    product = models.ForeignKey(Products,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    address = models.TextField()
    status = models.CharField(max_length=200)
    added = models.DateTimeField(default=now)
    def __str__(self) -> str:
        return self.product.name + " by "+self.user.name