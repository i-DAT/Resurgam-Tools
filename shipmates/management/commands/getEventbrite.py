import eventbrite
from shipmates.models import *
from django.core.management.base import BaseCommand, CommandError
from settings import authentications as auths

class Command(BaseCommand):
    help = 'Download Everything from eventbrite'
    
    
    def handle(self, *args, **options):
        print "Downloading"

        eb_auth_tokens = {
            'app_key':  auths.EVENTBRITE_APP_KEY, 
            'user_key': auths.EVENTBRITE_USER_KEY
        }

        eb_client = eventbrite.EventbriteClient(eb_auth_tokens)

        response = eb_client.event_get({'id':auths.EVENTBRITE_EVENT_ID})

        for ticket in response['event']['tickets']:
            a_type = TicketType()
            a_type.eb_id = ticket['ticket']['id']
            a_type.name = ticket['ticket']['name']
            a_type.save()

        response = eb_client.event_list_attendees({'id':auths.EVENTBRITE_EVENT_ID})

        for attendee in response['attendees']:
            a_holder = TicketHolder()
            a_holder.tickettype = TicketType.objects.get(eb_id=attendee['attendee']['ticket_id'])
            a_holder.name = attendee['attendee']['first_name'] + " " + attendee['attendee']['last_name']
            a_holder.barcode = attendee['attendee']['barcode']
            a_holder.email = attendee['attendee']['email']
            a_holder.quantity = attendee['attendee']['quantity']
            a_holder.order_type = attendee['attendee']['order_type']
            a_holder.save()