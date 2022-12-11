from django import forms

from website.models.choices import Speciality


class AppointmentForm(forms.Form):
    speciality = forms.ChoiceField(choices=Speciality.choices, required=True)
    slot = forms.DateTimeField(required=True)
