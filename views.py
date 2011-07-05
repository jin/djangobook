from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse 
import datetime


def hello(request):
    return HttpResponse("Hello World")


def current_datetime(request, template_name='dateapp/current_datetime.html'):
    current_date = datetime.datetime.now()
    return render_to_response(template_name, locals()) 


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('dateapp/hours_ahead.html', ({'hour_offset': offset, 'next_time': dt}))


def display_meta(request):
    return render_to_response('display_meta.html', {'request': request.META.items()})
