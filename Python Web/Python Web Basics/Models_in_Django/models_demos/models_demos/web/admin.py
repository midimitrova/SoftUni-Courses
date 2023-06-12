from django.contrib import admin

from models_demos.web.models import Employee, Department, Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'level')
    list_filter = ('level',)
    search_fields = ('first_name', 'last_name',)

    fieldsets = (
        (
            'Personal Info',
            {
                'fields': ('first_name', 'last_name', 'age'),
            }
        ),
        (
            'Professional Info',
            {
                'fields': ('level', 'years_of_experience'),
            }
        ),
        (
            'Company_info',
            {
                'fields': ('is_full_time', 'email', 'start_date'),
            }
        )
    )
