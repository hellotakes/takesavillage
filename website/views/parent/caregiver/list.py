import datetime

from django import forms
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_filters import FilterSet, BooleanFilter, CharFilter
from django_filters.views import FilterView

from website.models.caregiver import Caregiver


class CaregiverFilter(FilterSet):
    location = CharFilter(field_name='address__city', lookup_expr='icontains', label=_('Location'))

    class Meta:
        model = Caregiver
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


class CaregiverListView(FilterView):
    template_name = "website/parent/caregiver/list.html"
    model = Caregiver
    filterset_class = CaregiverFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['slots_by_specialist'] = []
        context['days'] = [datetime.date.today() + datetime.timedelta(days=i) for i in range(0, 7)]
        return context

