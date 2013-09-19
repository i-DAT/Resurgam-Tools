from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404, redirect

from django import forms

from django.contrib.auth.decorators import login_required

from models import *

def list_start_times(request):
	types_list = TicketType.objects.all()

	return render_to_response('list_start_times.html', {
        'types_list': types_list
    }, context_instance=RequestContext(request))

