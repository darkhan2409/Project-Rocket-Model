from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomManager


TYPE_CHOICES = [
    ('Lightweight – up to 5 tons of payload', 'Light'),
    ('Medium - from 5 to 20 tons', 'Medium'),
    ('Heavy – from 20 to 100 tons', 'Heavy'),
    ('Super heavy – over 100 tons', 'Super heavy')
]

FUEL_CHOICES = [
    ('Solid rocket engine', 'SRE'),
    ('Liquid rocket engine', 'Liquid rocket engine'),
    ('Hybrid', 'Hybrid')
]


class Rocket(models.Model):
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, blank=True, null=True)
    fuel_condition = models.CharField(max_length=50, choices=FUEL_CHOICES, blank=True, null=True)
    stages = models.IntegerField()
    image = models.ImageField(upload_to='rockets', blank=True, null=True)

    def __str__(self):
        return self.title


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = CustomManager()

