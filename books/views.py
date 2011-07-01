from django.shortcuts import render_to_response
from django.http import HttpResponse


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    if len(request.GET['q']):
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
