from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from website.models.client import Client
from website.models.specialist import Specialist, SpecialistAddress

admin.site.register(Specialist)
admin.site.register(SpecialistAddress, LeafletGeoAdmin)

admin.site.register(Client)
