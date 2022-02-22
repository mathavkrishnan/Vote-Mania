from django.db import models
from django.contrib.auth.models import User
class vote(models.Model):
    one = models.TextField(max_length=255)
    oneimage = models.ImageField()
    onevote = models.IntegerField(default=0)
    two = models.TextField(max_length=255)
    twoimage = models.ImageField()
    twovote = models.IntegerField(default=0)
class vote_likes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
