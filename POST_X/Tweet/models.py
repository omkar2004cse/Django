from django.db import models
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # limit tweet text to 140 characters (server-side validator)
    text = models.TextField(max_length=140, validators=[MaxLengthValidator(140)])
    photo=models.ImageField(upload_to='photos/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField( auto_now=True)


    def __str__(self):
        return f'{self.user}---{self.text[:10]}'
    