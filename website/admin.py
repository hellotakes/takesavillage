from django.contrib import admin

from website.models.appointment import Appointment
from website.models.business_hours import BusinessHours
from website.models.parent import Parent
from website.models.specialist import Specialist, SpecialistAddress

admin.site.register(Parent)

admin.site.register(Specialist)
admin.site.register(SpecialistAddress)
admin.site.register(BusinessHours)

admin.site.register(Appointment)
