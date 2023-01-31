from django.urls import path
#from . import views
from .views import HomeView, ReportDetail

urlpatterns = [
    #path('',views.home, name= 'home'),
    path('', HomeView.as_view(), name='home'),
    path('report/<int:pk>', ReportDetail.as_view(), name='details'), #primary key

]