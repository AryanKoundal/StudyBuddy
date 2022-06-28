import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from email.policy import default
from pickle import TRUE
from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from django.db.models.deletion import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import EmailField 

class User(AbstractUser):
    name = models.CharField(max_length=200,null=TRUE)
    email = models.EmailField(unique=True,null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=TRUE,default='avatar.svg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]