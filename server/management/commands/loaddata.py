import gspread
from django.core.management.base import BaseCommand
from server.models import Report, Category, Method, Account

sa = gspread.service_account()
sh = sa.open('Expenses report')
ws = sh.worksheet('django')
data = ws.get_all_values()

class Command(BaseCommand):
    help = 'load data'

    def handle(self, *args, **kwargs):

        for row in data[1:]:
            category_name = row[2]
            payment_method_name = row[5]
            account_name = row[1]

            account = Account.objects.get(name = account_name)
            category = Category.objects.get(name = category_name)
            payment_method = Method.objects.get(name = payment_method_name)

            report = Report(date = row[0], price = row[3], description = row[4])
            report.account = account
            report.category = category
            report.payment = payment_method
            report.save()
            