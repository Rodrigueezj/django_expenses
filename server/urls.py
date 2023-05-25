from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth.decorators import login_required

from . import views
from .views import HomeView, AddReport, DeleteReport

#app_name = 'server'
urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('', login_required(HomeView.as_view()), name='home'),
    path('chart/', login_required(views.chart_category), name='chart_category'),
    path('add_report/', login_required(views.AddReport), name = 'add_report'),
    path('delete_report/', login_required(DeleteReport.as_view()), name = 'delete_report'),
    path('ajax/load-categories/', login_required(views.load_categories), name = 'ajax_load_categories'),
    path('logout/', logout_then_login, name = 'logout')
]