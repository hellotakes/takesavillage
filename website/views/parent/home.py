from django.views.generic import TemplateView

from website.forms.parent.specialists import SearchSpecialistForm


class HomeView(TemplateView):
    template_name = "website/parent/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchSpecialistForm()
        return context
