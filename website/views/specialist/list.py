from django_filters import FilterSet
from django_filters.views import FilterView

from website.models.specialist import Specialist


class SpecialistFilter(FilterSet):
    class Meta:
        model = Specialist
        fields = [
            'first_name',
            'last_name',
            'speciality',
            'physical',
            'online',
            'language',
            'sex'
        ]


class SpecialistListView(FilterView):
    template_name = "website/specialist/list.html"
    model = Specialist
    filterset_class = SpecialistFilter
