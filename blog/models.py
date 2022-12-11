from django.db import models
from django.urls import reverse 

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50)
    post = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-view', args=(str(self.id)))


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name="blog_comment", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, default="")
    comment = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.article.title, self.name)
