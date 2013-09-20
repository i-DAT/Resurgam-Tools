from django.db import models

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


