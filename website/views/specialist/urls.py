from django.urls import path

from website.views.specialist.appointment.list import AppointmentListView
from website.views.specialist.home import HomeSpecialistView

app_name = 'website'
urlpatterns = [
    path("", HomeSpecialistView.as_view(), name="home"),
    path("appointments/", AppointmentListView.as_view(), name='appointment_list'),
]
