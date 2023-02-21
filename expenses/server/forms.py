from django import forms
from .models import Report
from bootstrap_datepicker_plus.widgets import DatePickerInput

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('author', 'payment', 'category', 'date', 'price', 'description')

        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'payment': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            }