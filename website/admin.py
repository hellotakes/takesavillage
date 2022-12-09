from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from website.models.parent import Parent
from website.models.specialist import Specialist, SpecialistAddress

admin.site.register(Specialist)
admin.site.register(SpecialistAddress, LeafletGeoAdmin)

admin.site.register(Parent)
