from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    project_title = models.CharField(max_length=100)
    project_description = models.TextField()
    languages_used = models.CharField(max_length=100)
    github_repo = models.CharField(max_length=100)

    def __str__(self):
        return self.project_title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    about = models.TextField()
    my_resume = models.FileField(blank=True, null=True)
    instagram = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    gmail = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
