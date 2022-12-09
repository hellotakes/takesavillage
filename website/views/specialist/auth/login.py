from django.contrib.auth.views import LoginView
from django.urls import reverse


class LoginView(LoginView):
    template_name = "website/specialist/auth/login.html"

    def get_default_redirect_url(self):
        return reverse("specialist:appointment_list")
