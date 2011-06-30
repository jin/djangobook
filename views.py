from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse 
import datetime


def hello(request):
    return HttpResponse("Hello World")


def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('dateapp/current_datetime.html', locals()) 


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hours, it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
