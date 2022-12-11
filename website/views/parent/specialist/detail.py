import datetime
from typing import List

from django.views.generic import DetailView

from website.business.appointment import compute_available_slots, group_slots_by_days
from website.forms.parent.appointment import AppointmentForm
from website.models.appointment import Appointment
from website.models.business_hours import BusinessHours
from website.models.specialist import Specialist


class SpecialistDetailView(DetailView):
    template_name = "website/parent/specialist/detail.html"
    model = Specialist

    context_object_name = "specialist"

    def get_appointments(self) -> List['Appointment']:
        return list(Appointment.objects.filter(
            specialist=self.object,
            from_time__range=(datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=6))
        ))

    def get_business_hours(self) -> List['BusinessHours']:
        return list(BusinessHours.objects.filter(specialist=self.object))

    def get_slots_available(self):
        days = [datetime.date.today() + datetime.timedelta(days=i) for i in range(0, 7)]
        slots_available = compute_available_slots(
            days,
            self.get_business_hours(),
            self.get_appointments()
        )
        return group_slots_by_days(days, slots_available)

    def get_context_data(self, **kwargs):
        return {
            'slots': self.get_slots_available(),
            'days': [datetime.date.today() + datetime.timedelta(days=i) for i in range(0, 7)],
            'form': AppointmentForm(),
            **super().get_context_data(**kwargs),
        }
