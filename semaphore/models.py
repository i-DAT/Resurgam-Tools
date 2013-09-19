from django.db import models

import pusher

from django.db.models.signals import post_save
from django.dispatch import receiver

from settings import authentications as auths

class Contact(models.Model):
    name = models.CharField(max_length=250)
    short = models.CharField(max_length=5, blank=True, null=True)
    phone_number = models.CharField(max_length=250)
    def __unicode__(self):
        return self.name

class Message(models.Model):
    contact =  models.ForeignKey(Contact)
    text = models.TextField(blank=True, null=True)
    recieved = models.DateTimeField(auto_now_add=True, null=True)
    def __unicode__(self):
        return self.contact.name + ': ' + self.text

def setupPusher():
    p = pusher.Pusher(
        app_id=auths.PUSHER_APP_ID,
        key=auths.PUSHER_KEY,
        secret=auths.PUSHER_SECRET
    )
    return p


@receiver(post_save, sender=Message)
def pushMessage(sender, instance, **kwargs):
    push = setupPusher()
    push['realtime'].trigger('new_message', {
        'sender': instance.contact.name,
        'text': instance.text,
    })
