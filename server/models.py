from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import redirect

class Account(models.Model):
    name = models.CharField(max_length=50)
    budget = models.FloatField()

    def __str__(self):
        return self.name

class Category(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    budget = models.FloatField()

    def __str__(self):
        return self.name

class Method(models.Model):
    name = models.CharField(max_length=50)
        
    def __str__(self):
        return self.name

class Report(models.Model):
    #profile = models.ForeignKey(User, on_delete=models.CASCADE)    
    date = models.DateField(default=timezone.now)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    payment = models.ForeignKey(Method, on_delete=models.CASCADE)
    description = models.CharField(max_length= 50, default='')
    
    def __str__(self):
        return self.description + ' | ' + str(self.date)

    def get_absolute_url(self):
        return redirect('/')
    
    class Meta:
        ordering = ('date',)