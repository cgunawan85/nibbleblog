from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='articles/photos/coverphotos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class Entry(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='articles/photos/entryphotos/', blank=True, null=True)
    restaurant_name = models.CharField(max_length=255)
    content = models.TextField()
    restaurant_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.restaurant_name

    class Meta:
        verbose_name_plural = "entries"

