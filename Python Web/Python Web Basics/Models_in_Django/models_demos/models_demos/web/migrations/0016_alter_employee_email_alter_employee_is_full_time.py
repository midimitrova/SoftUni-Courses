# Generated by Django 4.2.2 on 2023-06-10 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_employee_is_full_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_full_time',
            field=models.BooleanField(),
        ),
    ]
