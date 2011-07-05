from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('djangobook.views',
        (r'^hello/$', 'hello'),
        (r'^time/$', 'current_datetime'),
        (r'^time/plus/(?P<offset>\d{1,2})/$', 'hours_ahead'),
        (r'^admin/', include(admin.site.urls)),
        (r'^meta/$', 'display_meta'),
)

urlpatterns += patterns('djangobook.books.views',
        (r'^search-form/$', 'search_form'),
        (r'^search/$', 'search'),
)

urlpatterns += patterns('djangobook.contact.views',
        (r'^contact/$', 'contact'),
)
