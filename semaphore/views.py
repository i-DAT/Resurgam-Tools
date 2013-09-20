from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404, redirect

from django import forms

from django.contrib.auth.decorators import login_required

from twilio.twiml import Response
from django_twilio.decorators import twilio_view
from models import *

import datetime

from settings import authentications as auths

class send_form(forms.Form):
    text = forms.CharField(max_length=140, label='Your Message')


@login_required
def live_view(request):
    message_list = Message.objects.all().order_by("-recieved")
    a_send_form = send_form()

    return render_to_response('live_view.html', {
        'message_list': message_list,
        'send_form': a_send_form,
        'PUSHER_KEY': auths.PUSHER_KEY
    }, context_instance=RequestContext(request))


def live_view_send(request):
    success = False

    if request.method == "POST":
        a_send_form = send_form(request.POST)

        if a_send_form.is_valid():
            #Send from HQ Contact. Using XXX is not ideal, but works for now
            success = True
            the_contact = get_object_or_404(Contact, phone_number='XXX')
            the_message = Message()
            the_message.contact = the_contact
            the_message.text = a_send_form.cleaned_data['text']
            the_message.save()

        return render_to_response('form_return.json', {
            'success': success,
        }, context_instance=RequestContext(request))



@twilio_view
def sms_endpoint(request):


    #quick = blaaaaaaargh
    if request.method == "POST":
        the_contact = get_object_or_404(Contact, phone_number=request.POST['From'])
        the_message = Message()
        the_message.contact = the_contact
        the_message.text = request.POST['Body']
        the_message.save()

    r = Response()
    #r.sms('Thanks for the SMS message!')
    #print r
    return r