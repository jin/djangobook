from django.conf.urls.defaults import *
from djangobook.views import * 
from djangobook.books import views
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
        (r'^hello/$', hello),
        (r'^time/$', current_datetime),
        (r'^time/plus/(\d{1,2})/$', hours_ahead),
        (r'^admin/', include(admin.site.urls)),
        (r'^meta/$', display_meta),
        (r'^search-form/$', views.search_form),
        (r'^search/$', views.search),
)
