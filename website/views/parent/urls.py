from django.urls import path

from website.views.parent.appointment.create import AppointmentCreateView
from website.views.parent.home import HomeView
from website.views.parent.auth.login import LoginClientView
from website.views.parent.auth.logout import LogoutClientView
from website.views.parent.auth.signup import SignupView
from website.views.parent.specialist.detail import SpecialistDetailView
from website.views.parent.specialist.list import SpecialistListView

app_name = 'website'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginClientView.as_view(), name="login"),
    path('logout/', LogoutClientView.as_view(), name="logout"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('specialists/', SpecialistListView.as_view(), name='specialist_list'),
    path('specialist/<int:pk>', SpecialistDetailView.as_view(), name="specialist_detail"),
    path('appointment/<int:pk>', AppointmentCreateView.as_view(), name="appointment_create"),
]
