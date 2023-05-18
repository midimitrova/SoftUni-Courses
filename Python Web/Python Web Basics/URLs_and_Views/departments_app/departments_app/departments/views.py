from random import choice

from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def sample_view(request, *args, **kwargs):
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')


def show_departments(request, *args, **kwargs):
    body = f'path: {request.path}, args = {args}, kwargs = {kwargs}'
    return HttpResponse(body)


def show_departments_details(request, department_id):
    body = f'path: {request.path}, id: {department_id}'
    return HttpResponse(body)


def show_departments_with_render(request: HttpRequest, *args, **kwargs):
    context = {
        'page_title': 'Departments',
        'method': request.method,
        'order_by': request.GET.get('order_by', 'name'),
    }

    return render(request, 'departments/all.html', context)


def redirect_to_first_department(request):
    possible_order_by = ['name', 'age', 'id']
    order_by = choice(possible_order_by)
    return redirect('show departments details', department_id=13)


def show_not_found(request):
    # status_code = 404
    #
    # return HttpResponse('Error', status=status_code)
    return HttpResponseNotFound('This not found')
