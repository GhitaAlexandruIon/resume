from django.conf import settings
from django.db import models
from django.utils import timezone


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()


class Awards(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()


class Education(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()


class Experience(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()


class Interest(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()


class Skills(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

