from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404, redirect


from django import forms

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from models import *

import collections

from settings import authentications as auths


def make_player_form(quantity, first_player, first_player_email):
    fields = {}
    count = 1

    while count <= quantity:
        field_name = ''

        if count < 10:
            field_name = '0'+str(count)+ " Name"
        else:
            field_name = str(count)+" Name"

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

    count = 1

    while count <= quantity:
        field_name = ''

        if count < 10:
            field_name = '0'+str(count)+ " mail"
        else:
            field_name = str(count)+" mail"

        if count == 1:
            fields[field_name] = forms.CharField(
                initial=first_player_email,
                error_messages={'required': 'Please enter an email address'}
            )
        else:
            fields[field_name] = forms.CharField(
                error_messages={'required': 'Please enter an email address'}
            )
        count += 1

    
    fields = collections.OrderedDict(sorted(fields.items()))

    return type('player_form', (forms.BaseForm,), { 'base_fields': fields })


def visual(request):
    players_list = Player.objects.filter(arrived=True)

    return render_to_response('visual.html', {
        'players_list': players_list,
        'PUSHER_KEY': auths.PUSHER_KEY
    }, context_instance=RequestContext(request))

@login_required
def checked_in_players(request):
    players_list = Player.objects.filter(arrived=True)

    return render_to_response('checked_in_players.html', {
        'player_list': players_list
    }, context_instance=RequestContext(request))

@login_required
def list_start_times(request):
    types_list = TicketType.objects.all()

    return render_to_response('list_start_times.html', {
        'types_list': types_list
    }, context_instance=RequestContext(request))


@login_required
def list_ticket_holders(request, type_id):
    the_type = get_object_or_404(TicketType, pk=type_id)
    holder_list = TicketHolder.objects.filter(tickettype=the_type, checked_in=False)

    return render_to_response('list_ticket_holders.html', {
        'holder_list': holder_list,
        'start_time': the_type.name,
        'next_id': the_type.id + 1,
        'PUSHER_KEY': auths.PUSHER_KEY
    }, context_instance=RequestContext(request))


@login_required
def check_in_holders(request, holder_id):
    the_holder = get_object_or_404(TicketHolder, pk=holder_id)

    the_form = make_player_form(the_holder.quantity, the_holder.name, the_holder.email)

    success = False

    player_name = ""
    player_email = ""

    if request.method == "POST":
        the_form = the_form(request.POST)
        if the_form.is_valid():
            for key, value in the_form.cleaned_data.iteritems():
                #print key[3:]
                if key[3:] == 'Name':
                    player_name = value
                if key[3:] == 'mail':
                    player_email = value

                if player_name:
                    if player_email:
                        the_player = Player()
                        the_player.name = player_name
                        the_player.email = player_email
                        the_player.ticketholder = the_holder
                        the_player.save()
                        player_name = ""
                        player_email = ""

            the_holder.checked_in = True
            the_holder.save()

            return redirect('/shipmates/time/'+str(the_holder.tickettype.id)+'/')       
    

    return render_to_response('check_in_holders.html', {
        'the_holder': the_holder,
        'the_form': the_form
    }, context_instance=RequestContext(request))

@login_required
def check_in_players(request):
    player_list = Player.objects.filter(arrived=False).order_by('name')

    return render_to_response('check_in_players.html', {
        'player_list': player_list,
        'PUSHER_KEY': auths.PUSHER_KEY
    }, context_instance=RequestContext(request))

@csrf_exempt
def check_in_button(request):
    success = False
    if request.method == "POST":
        player_id = request.POST['player_id']
        the_player = get_object_or_404(Player, pk=player_id)
        the_player.arrived = True
        the_player.save()
        success = True

    return render_to_response('form_return.json', {
            'success': success,
    }, context_instance=RequestContext(request))

