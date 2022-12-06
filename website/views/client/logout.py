from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse


class LogoutClientView(LogoutView):

    def get_default_redirect_url(self):
        return reverse("home")
