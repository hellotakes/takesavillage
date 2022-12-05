from django import forms
from django.db import models
from django_filters import FilterSet, BooleanFilter, CharFilter
from django_filters.views import FilterView

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
    template_name = "website/specialist/list.html"
    model = Specialist
    filterset_class = SpecialistFilter
