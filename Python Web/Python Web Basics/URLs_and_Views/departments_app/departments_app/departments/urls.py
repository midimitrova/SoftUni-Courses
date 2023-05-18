from django.urls import path

from departments_app.departments.views import sample_view, show_departments, show_departments_details, \
    show_departments_with_render, redirect_to_first_department, show_not_found

urlpatterns = (
    path('', show_departments, name='show departments'),
    path('not-found/', show_not_found, name='not found'),
    path('redirect/', redirect_to_first_department, name='redirect demo'),
    path('<department_id>/', show_departments_details, name='show departments with string'),
    path('int/<int:department_id>/', show_departments_details, name='show departments details'),

)
