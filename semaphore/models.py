from django.db import models

import pusher

from django.db.models.signals import post_save
from django.dispatch import receiver

from settings import authentications as auths

from django_twilio.client import twilio_client



class Contact(models.Model):
    name = models.CharField(max_length=250)
    short = models.CharField(max_length=5, blank=True, null=True)
    phone_number = models.CharField(max_length=250)
    exclude_sms = models.BooleanField(default=False)
    def __unicode__(self):
        return self.name

@receiver(post_save, sender=Contact)
def sendWelcome(sender, instance, created, **kwargs):
    if created:
        if not instance.exclude_sms:
            return_sms = 'Hi ' + instance.name + ', you\'ve been added to the Resurgam text group. Respond to this number to send out a message to the group'
            sms = twilio_client.messages.create(
                body=return_sms,
                to=instance.phone_number,
                from_=auths.TWILIO_NUMBER,
            )


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

    return_sms = instance.contact.short + ": " + instance.text
    contact_list = Contact.objects.exclude(
        phone_number=instance.contact.phone_number
    ).filter(
        exclude_sms=False
    )

    for contact in contact_list:
        sms = twilio_client.messages.create(
            body=return_sms,
            to=contact.phone_number,
            from_=auths.TWILIO_NUMBER,
        )


