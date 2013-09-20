from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^admin/', include(admin.site.urls)),
     (r'^shipmates/time/(?P<type_id>\d+)/$', 'shipmates.views.list_ticket_holders'),
     (r'^shipmates/holder/(?P<holder_id>\d+)/$', 'shipmates.views.check_in_holders'),
     (r'^shipmates/visual/', 'shipmates.views.visual'),
     (r'^shipmates/', 'shipmates.views.list_start_times'),

     (r'^semaphore/sms/', 'semaphore.views.sms_endpoint'),
     (r'^semaphore/live/send/', 'semaphore.views.live_view_send'),
     (r'^semaphore/live/', 'semaphore.views.live_view'),
)
