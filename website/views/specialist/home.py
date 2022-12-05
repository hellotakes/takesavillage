from django.views.generic import TemplateView

from website.models.appointment import Appointment


class HomeSpecialistView(TemplateView):
    template_name = "website/specialist/home.html"

    def get_context_data(self, **kwargs):
        appointments = Appointment.objects.all()
        return {
            "appointments": appointments,
            **super().get_context_data(**kwargs)
        }
