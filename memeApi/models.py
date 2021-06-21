from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Meme(models.Model):
    userid = models.ForeignKey(
        User, related_name='userid', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media", blank=True)
    like = models.ForeignKey(User, related_name='like',
                             on_delete=models.CASCADE)
    comment_content = models.TextField(max_length=200)
    comment = models.ForeignKey(
        User, related_name='comment', on_delete=models.CASCADE)


class Count(models.Model):
    post = models.ForeignKey(Meme, related_name='post',
                             on_delete=models.CASCADE)
    likes = models.IntegerField()
    comments = models.IntegerField()


class img(models.Model):
    images = models.ImageField(upload_to="media")
