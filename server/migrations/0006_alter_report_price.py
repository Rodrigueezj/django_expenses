# Generated by Django 4.1.6 on 2023-02-27 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_alter_report_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]