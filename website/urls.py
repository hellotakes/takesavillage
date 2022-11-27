from django.urls import path

from website.views.home import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]