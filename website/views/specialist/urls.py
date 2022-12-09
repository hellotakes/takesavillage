from django.urls import path

from website.views.specialist.appointment.list import AppointmentListView
from website.views.specialist.home import HomeSpecialistView
from website.views.specialist.sign_up import SignUpView

app_name = 'website'
urlpatterns = [
    path("", HomeSpecialistView.as_view(), name="home"),
    path("appointments/", AppointmentListView.as_view(), name='appointment_list'),
    path("sign_up/", SignUpView.as_view(), name="sign_up"),
]
