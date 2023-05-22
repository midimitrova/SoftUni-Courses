from templates_demos.web.views import index
from django.urls import path

urlpatterns = (
    path('', index, name='index'),

)
