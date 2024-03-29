from datetime import date

from django.db import models
from django.urls import reverse


class AuditInfoMixin(models.Model):
    class Meta:
        abstract = True

    created_on = models.DateTimeField(
        auto_now_add=True,

    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )


class Department(AuditInfoMixin, models.Model):
    name = models.CharField(
        max_length=15,
    )
    slug = models.SlugField(
        unique=True,
    )

    def __str__(self):
        return f'ID: {self.pk} Name: {self.name}'

    def get_absolute_url(self):
        url = reverse('department-details', kwargs={
            'pk': self.pk,
            'slug': self.slug,
        })
        return url


class Project(AuditInfoMixin, models.Model):
    name = models.CharField(
        max_length=30
    )
    code_name = models.CharField(
        max_length=10,
        unique=True,
    )
    deadline = models.DateField()


class Employee(AuditInfoMixin, models.Model):
    class Meta:
        ordering = ('-years_of_experience', '-age',)

    LEVEL_JUNIOR = 'Junior'
    LEVEL_REGULAR = 'Regular'
    LEVEL_SENIOR = 'Senior'

    LEVELS = (
        (LEVEL_JUNIOR, LEVEL_JUNIOR),
        (LEVEL_REGULAR, LEVEL_REGULAR),
        (LEVEL_SENIOR, LEVEL_SENIOR),
    )

    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=50,
        null=True,
    )

    level = models.CharField(
        max_length=len(LEVEL_REGULAR),
        choices=LEVELS,
        verbose_name='Seniority level'

    )

    age = models.IntegerField(
        default=-1,
    )

    years_of_experience = models.PositiveIntegerField()

    review = models.TextField()

    start_date = models.DateField()

    email = models.EmailField(
        unique=True,
    )

    is_full_time = models.BooleanField(
        null=True,
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.RESTRICT,
    )

    projects = models.ManyToManyField(Project)

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def years_of_employment(self):
        return date.today() - self.start_date

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.fullname}; Department: {self.department}'
