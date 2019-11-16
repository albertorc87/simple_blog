"""Users URLs."""

# Django
from django.urls import path
from django.views.generic import TemplateView
# View
from users import views

urlpatterns = [
    path(
        route='login',
        view=TemplateView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path(
        route='registro',
        view=views.SignupView.as_view(),
        name='register'
    ),
]
