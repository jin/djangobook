from django.conf.urls.defaults import *
from djangobook.views import * 


urlpatterns = patterns('',
        (r'^hello/$', hello),
        (r'^time/$', current_datetime),
        (r'^time/plus/(\d{1,2})/$', hours_ahead),
)
