from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import CreateView

from website.models.client import Client


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    field_order = ['first_name', 'last_name']


class SignupView(CreateView):
    template_name = "website/client/signup.html"
    model = User
    form_class = SignUpForm

    def form_valid(self, form):
        response = super().form_valid(form)

        Client(user=self.object).save()

        return response

    def get_success_url(self):
        return reverse('home')
