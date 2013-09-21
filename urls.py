from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^admin/', include(admin.site.urls)),
     #registration, for dashboard logins
     (r'^accounts/', include('registration.backends.default.urls')),
     (r'^shipmates/time/(?P<type_id>\d+)/$', 'shipmates.views.list_ticket_holders'),
     (r'^shipmates/holder/(?P<holder_id>\d+)/$', 'shipmates.views.check_in_holders'),
     (r'^shipmates/visual/', 'shipmates.views.visual'),
     (r'^shipmates/', 'shipmates.views.list_start_times'),

     (r'^boarding/list/', 'shipmates.views.checked_in_players'),
     (r'^boarding/check_in/', 'shipmates.views.check_in_button'),
     (r'^boarding/', 'shipmates.views.check_in_players'),

     (r'^crew/list/', 'shipmates.views.checked_in_crew'),
     (r'^crew/check_in/', 'shipmates.views.check_in_button_crew'),
     (r'^crew/', 'shipmates.views.check_in_crew'),

     (r'^semaphore/sms/', 'semaphore.views.sms_endpoint'),
     (r'^semaphore/live/send/', 'semaphore.views.live_view_send'),
     (r'^semaphore/live/', 'semaphore.views.live_view'),

      #(r'^favicon\.ico$', RedirectView.as_view('/static/favicon.ico')),
)
