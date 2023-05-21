from django.urls import path

from challenges_templates.monthly_challenges_templates.views import monthly_challenge, monthly_challenge_by_number, index

urlpatterns = (
    # path('january/', jan_challenge),
    # path('february/', feb_challenge),
    path('', index, name='all-challenges'),
    path('<int:month>/', monthly_challenge_by_number),
    path('<month>/', monthly_challenge, name='month-challenge'),
)