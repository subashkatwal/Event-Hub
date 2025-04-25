# admin.py

from django.contrib import admin
from .models import Event, Registration

# admin.site.register(Event)
# Registering Event using the @admin.register decorator (no need for admin.site.register)
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_date', 'created_by', 'description')  # Add event details to the admin list
    search_fields = ('name', 'description', 'created_by__username')  # Search events by name, description, and creator
    list_filter = ('created_by', 'event_date')  # Filter events by creator and date

# Registering Registration using the @admin.register decorator (no need for admin.site.register)
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('get_user_name', 'get_user_email', 'event', 'registered_at')  # Display user and event info
    search_fields = ('user__username', 'user__email', 'event__name')  # Search by user name, email, or event name
    list_filter = ('event', 'registered_at')  # Filter registrations by event or registration date

    def get_user_name(self, obj):
        return obj.user.get_full_name() or obj.user.username  # Get full name or username if full name is empty
    get_user_name.short_description = 'User Name'  # Set custom label for the column

    def get_user_email(self, obj):
        return obj.user.email  # Display user's email
    get_user_email.short_description = 'User Email'  # Set custom label for the column
