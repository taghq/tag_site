from django.contrib import admin

from signup_form.models import Volunteer, Interest

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "created"]
    list_display_links = ('id','name', 'email')



admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Interest)
