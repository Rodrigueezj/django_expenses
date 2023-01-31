from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Report

# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Report
    template_name = 'home.html'

class ReportDetail(ListView):
    model = Report
    template_name = 'details.html'