# Generated by Django 4.1.3 on 2023-06-12 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0024_employee_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('code_name', models.CharField(max_length=10, unique=True)),
                ('deadline', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='projects',
            field=models.ManyToManyField(to='web.project'),
        ),
    ]
