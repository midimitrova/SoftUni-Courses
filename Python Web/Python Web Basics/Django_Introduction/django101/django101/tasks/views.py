from django.shortcuts import render
from django import http

from django101.tasks.models import Task


def show_bare_minimum(request):
    return http.HttpResponse('It works')


def get_all_tasks(request):
    all_tasks = Task.objects.all()
    print(list(all_tasks))


def visualize_tasks(request):
    all_tasks = Task.objects.order_by('id').all()
    context = {
        'title': 'The tasks app!',
        'tasks': all_tasks
    }

    return render(request, 'index.html', context)