from django.contrib import admin
from .models import Report, Method, Category, Account

admin.site.register(Report) # this in order to visualize the project on admin platform
admin.site.register(Method) 
admin.site.register(Category) 
admin.site.register(Account)