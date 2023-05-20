from django.urls import path

from monthly_challenges.challenges.views import monthly_challenge, monthly_challenge_by_number, index

urlpatterns = (
    # path('january/', jan_challenge),
    # path('february/', feb_challenge),
    path('', index),
    path('<int:month>/', monthly_challenge_by_number),
    path('<month>/', monthly_challenge, name='month-challenge'),
)