from django import forms


class CustomUserLoginForm(forms.Form):
    email = forms.EmailField(label='Адрес Mail облака')
    password = forms.CharField(label='Пароль от Mail облака')


class CustomUserRegistrationForm(forms.Form):
    name = forms.CharField(label='имя')
    surname = forms.CharField(label='фамилия')
    email = forms.EmailField(label='Адрес Mail облака')
    password = forms.CharField(label='Пароль от Mail облака', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите Пароль', widget=forms.PasswordInput)