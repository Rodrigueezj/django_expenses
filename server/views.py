from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView, UpdateView
from .models import Report, Category
from .forms import ReportForm
import plotly.express as px
from django.db.models import Sum

def BASE(request):
    reports = Report.objects.all()
    return render(request, 'index.html', {'reports': reports})

def list_report(request):
    reports = Report.objects.all()
    return render(request, 'list.html', {'reports': reports})

def edit_report(request, id):
    report = Report.objects.get(id=id)
    
    if request.method == 'GET':
        report_form = ReportForm(instance = report)

    else:
        report_form = ReportForm(request.POST, instance = report)
        if report_form.is_valid():
            report_form.save()
        redirect('list_report')

class UpdateReport(UpdateView):
    model = Report
    template_name = 'add_report.html'
    form_class = ReportForm
    success_url = reverse_lazy('list_report')

class DeleteReport(DeleteView):
    model = Report
    template_name = 'delete_report.html'

class DetailReport(DetailView):
    model = Report
    template_name = 'detail.html'

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