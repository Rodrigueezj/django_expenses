from django.urls import path
from . import views
from .views import HomeView, AddReport, DeleteReport

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('exit/', views.exit, name='exit'),
    path('add_report/', AddReport.as_view(), name = 'add_report'),
    path('delete_report/', DeleteReport.as_view(), name = 'delete_report'),
]