import datetime

from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView

from website.models.appointment import Appointment
from website.models.specialist import Specialist


class AppointmentForm(forms.Form):
    slot = forms.DateTimeField(required=True)


class AppointmentCreateView(LoginRequiredMixin, FormView, SuccessMessageMixin):
    template_name = "website/parent/specialist/detail.html"

    form_class = AppointmentForm

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        Appointment(
            specialist=Specialist.objects.get(pk=self.kwargs['pk']),
            client=self.request.user.client,
            from_time=form.cleaned_data['slot'],
            duration=datetime.timedelta(minutes=30),
        ).save()

        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return _('Booked')

    def get_success_url(self):
        return reverse("specialist_detail", kwargs={"pk": self.kwargs['pk']})
