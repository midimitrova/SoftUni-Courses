# Generated by Django 4.1.3 on 2023-06-09 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_employee_age_employee_last_name_employee_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=5),
        ),
    ]
