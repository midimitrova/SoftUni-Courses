from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# def jan_challenge(request):
#     return HttpResponse('Eat no meat for the entire month!')
#
#
# def feb_challenge(request):
#     return HttpResponse('Walk for at least 20 minutes every day!')

monthly_challenges = {
    'january': 'Eat no meat for the entire month!',
    'february': 'Walk for at least 20 minutes every day!',
    'march': 'Learn Django for at least 20 minutes every day!',
    'april': 'One month of sugar detox!',
    'may': 'One month of running 1 mile each day!',
    'june': 'One month of yoga every day!',
    'july': 'One month of social media detox!',
    'august': 'One month of caffeine detox!',
    'september': 'One month of eating only at home or home-cooked meal!',
    'october': 'One month without alcohol and soda!',
    'november': 'One month of no Netflix and TV!',
    'december': 'One month of daily reading for at least 30 minutes!',
}


def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month!')

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('This month is not supported!')
