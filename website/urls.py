from django.urls import path, include

from website.views.client.appointment.make import AppointmentCreateView
from website.views.client.home import HomeView
from website.views.client.specialist.detail import SpecialistDetailView
from website.views.client.specialist.list import SpecialistListView
from website.views.specialist.appointments import AppointmentView
from website.views.specialist.home import HomeSpecialistView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('specialists/', SpecialistListView.as_view(), name='specialist_list'),
    path('specialist/<int:pk>', SpecialistDetailView.as_view(), name="specialist_detail"),
    path('appointment/<int:pk>', AppointmentCreateView.as_view(), name="appointment_create"),
    path('pro/', include([
        path("", HomeSpecialistView.as_view(), name="pro_home"),
        path("appointments/", AppointmentView.as_view(), name='appointments'),
    ]))

]
