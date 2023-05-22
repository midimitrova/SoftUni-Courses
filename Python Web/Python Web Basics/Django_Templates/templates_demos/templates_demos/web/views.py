import random
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'Name: {self.name}, Age: {self.age}'


def index(request):
    context = {
        'title': 'SoftUni Homepage',
        'value': random.random(),
        'info': {
            'address': 'Sofia',
        },
        'student': Student('Maria', 28),
        'student_info': Student('Maria', 28).get_info(),
        'now': datetime.now(),
        'students': ['Maria', 'Ivan', 'John', 'Emma'],
        # 'students': [],
        'values': list(range(20)),
    }

    return render(request, 'index.html', context)
