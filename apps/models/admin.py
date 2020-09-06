from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Event, Ticket
# Register your models here.

admin.site.unregister(Group)
admin.site.register(Event)
admin.site.register(Ticket)