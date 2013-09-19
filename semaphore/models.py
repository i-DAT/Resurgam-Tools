from django.db import models

# Create your models here.
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
