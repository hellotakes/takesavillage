from django.views.generic import TemplateView


class HomeSpecialistView(TemplateView):
    template_name = "website/specialist/home.html"
