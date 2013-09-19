from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404, redirect


from django import forms

from django.contrib.auth.decorators import login_required

from models import *

import collections

def make_player_form(quantity, first_player):
    fields = {}
    count = 1

    while count <= quantity:
        field_name = ''

        if count < 10:
            field_name = '0'+str(count)
        else:
            field_name = str(count)

        if count == 1:
            fields[field_name] = forms.CharField(
                initial=first_player,
                error_messages={'required': 'Please enter a name'}
            )
        else:
            fields[field_name] = forms.CharField(
                error_messages={'required': 'Please enter a name'}
            )
        count += 1

        fields = collections.OrderedDict(sorted(fields.items()))

    return type('player_form', (forms.BaseForm,), { 'base_fields': fields })

def visual(request):
    players_list = Player.objects.all()

    return render_to_response('visual.html', {
        'players_list': players_list
    }, context_instance=RequestContext(request))

def list_start_times(request):
    types_list = TicketType.objects.all()

    return render_to_response('list_start_times.html', {
        'types_list': types_list
    }, context_instance=RequestContext(request))


def list_ticket_holders(request, type_id):
    the_type = get_object_or_404(TicketType, pk=type_id)
    holder_list = TicketHolder.objects.filter(tickettype=the_type, checked_in=False)

    return render_to_response('list_ticket_holders.html', {
        'holder_list': holder_list,
        'start_time': the_type.name,
        'next_id': the_type.id + 1
    }, context_instance=RequestContext(request))

def check_in_holders(request, holder_id):
    the_holder = get_object_or_404(TicketHolder, pk=holder_id)

    the_form = make_player_form(the_holder.quantity, the_holder.name)

    success = False

    if request.method == "POST":
        the_form = the_form(request.POST)
        if the_form.is_valid():
            for key, value in the_form.cleaned_data.iteritems():
                the_player = Player()
                the_player.name = value
                the_player.ticketholder = the_holder
                the_player.save()

            the_holder.checked_in = True
            the_holder.save()

            return redirect('/shipmates/time/'+str(the_holder.tickettype.id)+'/')       
    

    return render_to_response('check_in_holders.html', {
        'the_holder': the_holder,
        'the_form': the_form
    }, context_instance=RequestContext(request))

