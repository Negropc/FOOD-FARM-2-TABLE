from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('subject', 'status', 'priority', 'requester_email', 'created_at')
    list_filter = ('status', 'priority')
    search_fields = ('subject', 'requester_email', 'description')
