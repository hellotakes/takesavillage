import datetime
from typing import List

from django.views.generic import DetailView

from website.business.booking import Booking
from website.models.appointment import Appointment
from website.models.specialist import Specialist


class SpecialistDetailView(DetailView):
    template_name = "website/specialist/detail.html"
    model = Specialist

    context_object_name = "specialist"

    def get_appointments(self) -> List['datetime.datetime']:
        appointments = Appointment.objects.filter(
            specialist=self.object,
            from_time__gte=datetime.datetime.now()
        )
        return [appointment.from_time for appointment in appointments]

    def get_context_data(self, **kwargs):
        slots_available = Booking(datetime.date.today(), self.get_appointments()).as_list()
        return {
            'slots': slots_available,
            **super().get_context_data(**kwargs),
        }
