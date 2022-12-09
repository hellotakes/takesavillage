import datetime
from typing import Iterable, List, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic import WeekArchiveView, TemplateView

from website.models.appointment import Appointment


class AppointmentListView(LoginRequiredMixin, TemplateView):
    template_name = "website/specialist/appointment/list.html"


class AppointmentFeedsView(LoginRequiredMixin, WeekArchiveView):
    template_name = "website/specialist/appointment/list.html"
    date_field = 'from_time'
    week_format = "%W"
    allow_future = True
    allow_empty = True

    def get_queryset(self):
        return Appointment.objects.filter(specialist__user=self.request.user)

    @property
    def date(self) -> 'datetime.datetime':
        return datetime.datetime.fromisoformat(self.request.GET['start'])

    @property
    def year(self) -> int:
        return self.date.year

    @property
    def week(self) -> int:
        return self.date.isocalendar()[1]

    def get(self, request, *args, **kwargs):
        date_list, object_list, extra_context = self.get_dated_items()
        return JsonResponse(appointments_to_json(object_list or []), safe=False)


def appointments_to_json(appointments: Iterable['Appointment']) -> List[Dict]:
    return [
        dict(
            title=f"{appointment.parent.full_name}",
            start=appointment.from_time.isoformat(),
            end=(appointment.from_time + appointment.duration).isoformat()
        ) for appointment in appointments
    ]
