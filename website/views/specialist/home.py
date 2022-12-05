from django.views.generic import TemplateView

from website.models.appointment import Appointment


class HomeSpecialistView(TemplateView):
    template_name = "website/specialist/home.html"
