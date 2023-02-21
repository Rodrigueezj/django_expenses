from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView
from .models import Report
from .forms import ReportForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout


@method_decorator(login_required, name='dispatch')
class HomeView(ListView):
    model = Report
    template_name = 'home.html'

class AddReport(CreateView):
    model = Report
    form_class = ReportForm
    template_name = 'add_report.html'

class DeleteReport(DeleteView):
    model = Report
    template_name = 'delete_report.html'

def exit(request):
    logout(request)
    return redirect('/')