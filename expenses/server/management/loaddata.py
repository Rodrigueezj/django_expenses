import gspread
from django.core.management.base import BaseCommand
from models import Report, Category, Method

sa = gspread.service_account()
sh = sa.open('Expenses report')
ws = sh.worksheet('django')
data = ws.get_all_values()

# class Command(BaseCommand):
    
#     def handle(self, *args, **kwargs):

#         for row in data[1:]:
#             category_name = row[2]
#             payment_method_name = row[5]

#             category = Category.objects.get(name = category_name)
#             payment_method = Method.objects.get(name = payment_method_name)

#             report = Report(date = row[0], account = row[1], price = row[3], description = row[4])
#             report.category = category
#             report.payment = payment_method
#             report.save()
            