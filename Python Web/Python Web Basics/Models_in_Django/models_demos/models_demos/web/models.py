from django.db import models


class Employee(models.Model):
    first_name = models.CharField(
        max_length=30
    )

    years_of_experience = models.PositiveIntegerField()

    review = models.TextField()

    start_date = models.DateField()

    email = models.EmailField()

    created_on = models.DateTimeField(
        auto_now_add=True,

    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )
