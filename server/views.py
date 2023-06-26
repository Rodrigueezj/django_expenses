from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView
from .models import Report, Category, Account
from .forms import ReportForm
import plotly.express as px
from django.db.models import Sum
from django.contrib.auth.forms import UserCreationForm

def registration(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/registration.html', context)

def BASE(request):
    reports = Report.objects.all()
    return render(request, 'index.html', {'reports': reports})


def list_report(request):
    reports = Report.objects.all()
    return render(request, 'list.html', {'reports': reports})

def list_account(request):
    accounts = Account.objects.all()
    return render(request, 'list_account.html', {'accounts': accounts})

def list_category(request):
    categories = Category.objects.all()
    return render(request, 'list_category.html', {'categories': categories})


class UpdateReport(UpdateView):
    model = Report
    template_name = 'add_report.html'
    form_class = ReportForm
    success_url = reverse_lazy('list_report')

class UpdateAccount(UpdateView):
    model = Report
    template_name = 'add_account.html'
    form_class = ReportForm
    success_url = reverse_lazy('list_account')

class UpdateCategory(UpdateView):
    model = Category
    template_name = 'add_category.html'
    form_class = ReportForm
    success_url = reverse_lazy('list_account')


class DeleteReport(DeleteView):
    model = Report
    success_url = reverse_lazy('list_report')

class DeleteAccount(DeleteView):
    model = Account
    success_url = reverse_lazy('list_account')

class DeleteCategory(DeleteView):
    model = Category
    success_url = reverse_lazy('list_category')


def add_report(request):
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_report')
    return render(request, 'add_report.html', {'form': form})

def chart_category(request):
    sums = Report.objects.values('category__name').annotate(total_price=Sum('price'))
    fig = px.pie(sums, values='total_price', names='category__name')
    chart = fig.to_html()
    context = {'chart_category': chart}
    return render(request, 'chart.html', context)

def load_categories(request):
    account_id = request.GET.get('account_id')
    categories = Category.objects.filter(account_id=account_id).all()
    return render(request, 'category_dropdown_list_options.html', {'categories': categories})