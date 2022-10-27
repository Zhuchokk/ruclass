from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class Login(FormView):
    template_name = 'education/login.html'
    form_class = CustomUserLoginForm

    def get_success_url(self):
        return reverse('Home')

    def form_valid(self, form):
        data = form.cleaned_data
        user = authenticate(email=data['email'], password=data['password'])
        print(user)
        if user:
            login(self.request, user)
            return super(Login, self).form_valid(form)
        else:

            form.add_error(None, 'Неверный логин или пароль')
            return super(Login, self).form_invalid(form)


class Register(FormView):
    template_name = 'education/register.html'
    form_class = CustomUserRegistrationForm

    def get_success_url(self):
        return reverse('Home')

    def form_valid(self, form):
        data = form.cleaned_data
        if data['password'] == data['password2']:
            user = User.objects.create_user(username=data['name'] + '_' + data['surname'], email=data['email'], password=data['password'])
            login(self.request, user)
        else:
            form.add_error(None, 'Неверно указан пароль')
            return super(Register, self).form_invalid(form)

        return super(Register, self).form_valid(form)


class HomeCheck(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Home.as_view()(request)
        else:
            # return redirect("Login")
            return redirect('Login')


class Home(View):
    def get(self, request):
        return render(request, 'education/home.html')