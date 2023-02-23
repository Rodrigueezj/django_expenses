from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView
from .models import Report, Category
from .forms import ReportForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.http import HttpRequest

@method_decorator(login_required, name='dispatch')
class HomeView(ListView):
    model = Report
    template_name = 'home.html'

def AddReport(request):
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_report')
    return render(request, 'add_report.html', {'form': form})

class DeleteReport(DeleteView):
    model = Report
    template_name = 'delete_report.html'

def load_categories(request):
    account_id = request.GET.get('account_id')#here is the problem
    categories = Category.objects.filter(account_id=account_id).all()
    return render(request, 'category_dropdown_list_options.html', {'categories': categories})

def exit(request):
    logout(request)
    return redirect('/')