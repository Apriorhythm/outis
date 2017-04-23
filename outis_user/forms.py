from django import forms

from .models import OutisUser

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    # Meta are Information of you class
    class Meta:
        model = OutisUser
        fields = ['username', 'password']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = OutisUser
        fields = ['username', 'password']


