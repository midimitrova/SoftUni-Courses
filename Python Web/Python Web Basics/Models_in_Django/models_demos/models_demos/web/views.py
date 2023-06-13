from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from models_demos.web.models import Employee, Department


def index(request):
    employees = Employee.objects.all()
    employees2 = Employee.objects.filter(department__name='Engeneering').filter(age__gte=20) \
        # .order_by('last_name','first_name')

    department = Department.objects.get(pk=2)
    # get_object_or_404(Employee, level=Employee.LEVEL_REGULAR)
    context = {
        'employees': employees,
        'employees2': employees2,
        'department': department,
    }

    return render(request, 'index.html', context)


def delete_employee(request, pk):
    department_pk = 2
    Employee.objects.filter(department_id=department_pk).delete()
    get_object_or_404(Department, pk=department_pk).delete()
    # employee = get_object_or_404(Employee, pk=pk)
    # employee.delete()
    return redirect('index')


def department_details(request, pk, slug):
    context = {
        'department': get_object_or_404(Department, pk=pk, slug=slug)
    }
    return render(request, 'department-details.html', context)
