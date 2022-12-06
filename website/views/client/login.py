from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect


class LoginClientView(LoginView):
    template_name = "website/client/login.html"

    def get_default_redirect_url(self):
        return redirect("home")
