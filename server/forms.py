from django import forms
from .models import Report, Account, Category
from bootstrap_datepicker_plus.widgets import DatePickerInput

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'

        widgets = {
            #'profile': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'account': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'payment': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            }
            
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

        self.fields['category'].queryset = Account.objects.none() #hace que no salga ninguna opción en category

        if 'account' in self.data:
            try:
                account_id = int(self.data.get('account'))
                self.fields['category'].queryset = Category.objects.filter(account_id = account_id).order_by('name')
            except (ValueError, TypeError):
                pass

        elif self.instance.pk:
            self.fields['category'].queryset = self.instance.account.category_set.order_by('name')

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

        widgets = {
            #'profile': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.DateInput(attrs={'class': 'form-control'}),
            }
      