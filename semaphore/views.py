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

def live_view(request):
    message_list = Message.objects.all().order_by("-recieved")

    return render_to_response('live_view.html', {
        'message_list': message_list,
        'PUSHER_KEY': auths.PUSHER_KEY
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