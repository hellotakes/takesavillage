import datetime
from typing import Iterable

from django import forms
from django.db import models
from django_filters import FilterSet, BooleanFilter, CharFilter
from django_filters.views import FilterView

from website.business.appointment import compute_available_slots, group_slots_by_days
from website.models.appointment import Appointment
from website.models.business_hours import BusinessHours
from website.models.specialist import Specialist


class SpecialistFilter(FilterSet):
    class Meta:
        model = Specialist
        fields = [
            'speciality',
            'physical',
            'online',
            'language',
            'sex'
        ]
        filter_overrides = {
            models.CharField: {
                'filter_class': CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
            models.BooleanField: {
                'filter_class': BooleanFilter,
                'extra': lambda f: {
                    'widget': forms.CheckboxInput,
                },
            },
        }


class SpecialistListView(FilterView):
    template_name = "website/parent/specialist/list.html"
    model = Specialist
    filterset_class = SpecialistFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['slots_by_specialist'] = self.get_specialists_slots(object_list) if object_list else []
        context['days'] = [datetime.date.today() + datetime.timedelta(days=i) for i in range(0, 7)]
        return context

    def get_specialists_slots(self, specialists: Iterable['Specialist']):
        days = [datetime.date.today() + datetime.timedelta(days=i) for i in range(0, 7)]

        result = []
        for specialist in specialists:
            appointments = list(Appointment.objects.filter(
                specialist=specialist,
                from_time__range=(datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=6))
            ))
            business_hours = list(BusinessHours.objects.filter(specialist=specialist))
            slots_available = compute_available_slots(
                days,
                business_hours,
                appointments
            )

            result.append(group_slots_by_days(days, slots_available))
        return result
