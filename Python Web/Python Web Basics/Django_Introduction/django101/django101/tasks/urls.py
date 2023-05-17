from django.urls import path

from django101.tasks.views import show_bare_minimum, get_all_tasks, visualize_tasks

urlpatterns = (
    path('', visualize_tasks),
    path('it-works/', show_bare_minimum),
    path('all/', get_all_tasks),
)