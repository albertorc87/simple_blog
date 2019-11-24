"""Users URLs."""

# Django
from django.urls import path
from django.views.generic import TemplateView
# View
from users import views

urlpatterns = [
    path(
        route='login',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='registro',
        view=views.SignupView.as_view(),
        name='register'
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='registro_completado/',
        view=TemplateView.as_view(template_name='users/registerok.html'),
        name='registerok'
    ),
]
