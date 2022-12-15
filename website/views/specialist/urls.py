from django.urls import path

from website.views.specialist.home import HomeSpecialistView

app_name = 'website'
urlpatterns = [
    path("", HomeSpecialistView.as_view(), name="home"),
]
