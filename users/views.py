from django.shortcuts import render

from django.views.generic import FormView
from django.urls import reverse, reverse_lazy

# Forms
from users.forms import SignupForm


class SignupView(FormView):
    """Users sign up view."""

    template_name = 'users/register.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login', kwargs={'message': 'Tu usuario ha sido creado correctamente :)'})

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)