from django.urls import path

from website.views.specialist.appointment.list import AppointmentFeedsView, AppointmentListView
from website.views.specialist.auth.login import LoginView
from website.views.specialist.home import HomeSpecialistView
from website.views.specialist.sign_up import SignUpView

app_name = 'website'
urlpatterns = [
    path("", HomeSpecialistView.as_view(), name="home"),
    path("appointments/", AppointmentListView.as_view(), name='appointment_list'),
    path("appointments/feeds/", AppointmentFeedsView.as_view(), name='appointment_feeds'),
    path("sign_up/", SignUpView.as_view(), name="sign_up"),
    path("login/", LoginView.as_view(), name="login"),
]
