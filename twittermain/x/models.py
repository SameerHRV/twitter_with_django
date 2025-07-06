from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Create a model for tweets
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # user who tweeted
    text = models.TextField(max_length=140) # text of tweet
    photo = models.ImageField(upload_to='media/tweets/', blank=True, null=True) # photo of tweet
    created_at = models.DateTimeField(auto_now_add=True) # date and time of tweet
    updated_at = models.DateTimeField(auto_now=True) # date and time of tweet
    
    def __str__(self):
        return f'{self.user.username} tweeted {self.text[:10]}' # string representation of tweet
