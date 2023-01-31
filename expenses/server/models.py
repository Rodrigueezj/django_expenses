from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #means when user deleted, pages deleted
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)