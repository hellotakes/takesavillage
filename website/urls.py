from django.urls import path

from website.views.home import HomeView
from website.views.specialist.detail import SpecialistDetailView
from website.views.specialist.list import SpecialistListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('specialists/', SpecialistListView.as_view(), name='specialist_list'),
    path('specialist/<int:pk>', SpecialistDetailView.as_view(), name="specialist_detail"),

]
