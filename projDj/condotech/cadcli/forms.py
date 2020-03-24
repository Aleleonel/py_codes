from django import forms


class LoginForm(forms.Form):
    name = forms.CharField(label='Seu nome', max_length=25)
    password = forms.CharField(label='Digite sua senha', max_length=8)
