from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView
from .models import Report, Category
from .forms import ReportForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
import plotly.express as px
from django.db.models import Sum

@method_decorator(login_required, name='dispatch') 
class HomeView(ListView):
    model = Report
    template_name = 'home.html'

def chart(request):
    sums = Report.objects.values('category__name').annotate(total_price=Sum('price')) #here is the error

    fig = px.pie(sums, values='total_price', names='category__name')
    print(sums)

    chart = fig.to_html()
    context = {'chart': chart}
    return render(request, 'chart.html', context)

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
    account_id = request.GET.get('account_id')
    categories = Category.objects.filter(account_id=account_id).all()
    return render(request, 'category_dropdown_list_options.html', {'categories': categories})

def exit(request):
    logout(request)
    return redirect('/')