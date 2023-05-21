from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string


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
    'december': None
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, 'challenges/index.html', {
        'months': months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('<h1>This month is not supported!</h1>')

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            'title': month,
            'text': challenge_text,
        })
    except:
        response_data = render_to_string('404.html')
        return HttpResponseNotFound(response_data)


