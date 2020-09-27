"""User forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.Form):
    """Sign up form."""

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )
    username = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.TextInput()
    )
    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )


    def clean(self):
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        """Verify password confirmation match."""
        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        try:
            User.objects.get(email=data['email'])
        except User.DoesNotExist:
            pass
        else:
            raise forms.ValidationError('El email ya existe')

        try:
            User.objects.get(username=data['username'])
        except User.DoesNotExist:
            pass
        else:
            raise forms.ValidationError('El nombre de usuario ya existe')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()