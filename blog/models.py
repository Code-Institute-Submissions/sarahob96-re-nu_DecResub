from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50)
    post = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-view', args=(str(self.id)))


class Comment(models.Model):
    post = models.ForeignKey(Article, related_name="blog_comment", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.post.title
