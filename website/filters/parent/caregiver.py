from django import forms
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_filters import FilterSet, CharFilter, BooleanFilter, ChoiceFilter

from website.models.caregiver import Caregiver
from website.models.choices import Language, Speciality


class CaregiverFilter(FilterSet):
    location = CharFilter(field_name='address__city', lookup_expr='icontains', label=_('Location'))
    speciality = ChoiceFilter(
        choices=Speciality.choices,
        method='filter_by_speciality',
        label=_('Speciality')
    )
    language = ChoiceFilter(
        choices=Language.choices,
        method='filter_by_language',
        label=_('Language')
    )

    class Meta:
        model = Caregiver
        fields = [
            'physical',
            'online',
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

    def filter_by_language(self, queryset, name, value):
        return queryset.filter(languages__contains=[value])

    def filter_by_speciality(self, queryset, name, value):
        return queryset.filter(specialities__speciality=value)
