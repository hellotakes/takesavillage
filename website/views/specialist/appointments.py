from django import forms
from django.http import JsonResponse
from django.views import View

from website.models.appointment import Appointment


class AppointmentForm(forms.Form):
    start = forms.DateTimeField()
    end = forms.DateTimeField()


class AppointmentView(View):
    def get(self, *args, **kwargs):
        form = AppointmentForm(self.request.GET)
        if not form.is_valid():
            return JsonResponse([])

        return JsonResponse(self.get_appointments(), safe=False)

    def get_appointments(self):
        appointments = Appointment.objects.all()
        return [
            dict(
                title="Rendez - vous",
                start=appointment.from_time.isoformat(),
                end=(appointment.from_time + appointment.duration).isoformat()
            )
            for appointment in appointments
        ]



