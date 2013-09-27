from models import *

from django.contrib import admin
from shipmates.actions import export_as_xls

admin.site.register(TicketType)
admin.site.register(TicketHolder)
admin.site.register(Player)
admin.site.register(Crew)

class MyAdmin(admin.ModelAdmin):
    actions = [export_as_xls]

admin.site.add_action(export_as_xls)