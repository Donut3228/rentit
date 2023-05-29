from django import forms
from .models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if not confirm_password or password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password
