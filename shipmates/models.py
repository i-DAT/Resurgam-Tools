from django.db import models

import pusher

from django.db.models.signals import post_save
from django.dispatch import receiver

from settings import authentications as auths

def setupPusher():
    p = pusher.Pusher(
        app_id=auths.PUSHER_APP_ID,
        key=auths.PUSHER_KEY,
        secret=auths.PUSHER_SECRET
    )
    return p


class TicketType(models.Model):
    eb_id = models.IntegerField()
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

class TicketHolder(models.Model):
    name = models.CharField(max_length=500)
    order_type = models.CharField(max_length=250)
    barcode = models.CharField(max_length=250)
    email = models.EmailField()
    quantity = models.IntegerField()
    tickettype = models.ForeignKey(TicketType)
    checked_in = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Player(models.Model):
    ticketholder = models.ForeignKey(TicketHolder)
    name = models.CharField(max_length=500)
    email = models.EmailField(blank=True, null=True)
    arrived = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Crew(models.Model):
    name = models.CharField(max_length=500)
    arrived = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

@receiver(post_save, sender=TicketHolder)
def pushHolder(sender, instance, **kwargs):
    if instance.checked_in:
        push = setupPusher()
        push['arrivals'].trigger('checked_in', {
            'holder_id': instance.id
        })


@receiver(post_save, sender=Player)
def pushMessage(sender, instance, **kwargs):
    if instance.arrived:
        push = setupPusher()
        push['boarding'].trigger('checked_in', {
            'player_id': instance.id,
            'player_name': instance.name
        })

@receiver(post_save, sender=Crew)
def pushCrew(sender, instance, **kwargs):
    if instance.arrived:
        push = setupPusher()
        push['crew'].trigger('checked_in', {
            'crew_id': instance.id
        })

