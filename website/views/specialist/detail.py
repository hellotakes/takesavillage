from django.views.generic import DetailView

from website.models.specialist import Specialist


class SpecialistDetailView(DetailView):
    template_name = "website/specialist/detail.html"
    model = Specialist

    context_object_name = "specialist"
