from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView

from website.forms.specialist.sign_up import SignUpForm


class SignUpView(SuccessMessageMixin, FormView):
    template_name = "website/specialist/sign_up.html"
    form_class = SignUpForm
    success_message = _("We will proceed your request.")

    def form_valid(self, form):
        # send mail
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("specialist:home")
