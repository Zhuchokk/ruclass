from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, FormMixin
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic.list import ListView
from .models import Course, Task, Work
from django.utils import timezone


class Login(FormView):
    template_name = 'education/login.html'
    form_class = CustomUserLoginForm

    def get_success_url(self):
        return reverse('Home')

    def form_valid(self, form):
        data = form.cleaned_data
        user = authenticate(username=data['email'], password=data['password'])
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
            user.name = data['name']
            user.surname = data['surname']
            login(self.request, user)
        else:
            form.add_error(None, 'Неверно указан пароль')
            return super(Register, self).form_invalid(form)

        return super(Register, self).form_valid(form)


class Home(ListView):

    template_name = "education/home.html"
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_paginated']= False
        # context['object_list'] = Course.objects.filter(members__email=self.request.user.email)
        # context['task_list'] = []
        # for course in context['object_list']:
        #     context['task_list'].append(Task.objects.filter(course=course, deadline__gt=timezone.now()))
        courses = Course.objects.filter(members__email=self.request.user.email)
        tasks = []
        for course in courses:
            tasks.append(Task.objects.filter(course=course, deadline__gt=timezone.now()))
        context['object_list'] = zip(courses, tasks)
        print(context['object_list'],  "- Home")
        return context

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return self.get(request, *args, **kwargs)
        else:
            return redirect("Login")


class OneCourse(ListView):
    template_name = "education/course.html"
    model = Task

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        code = self.kwargs.get('code')

        context['object_list'] = Task.objects.filter(course__code=code)
        print(context['object_list'], "- OneCourse")
        return context

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return self.get(request, *args, **kwargs)
        else:
            return redirect("Login")


class OneTask(FormView):
    form_class = WorkForm
    template_name = 'education/task.html'

    def get_context_data(self,**kwargs):
        context = super(OneTask, self).get_context_data(**kwargs)
        print(self.kwargs.get('code'))
        context.update({'task': Task.objects.get(code=self.kwargs.get('code'))})
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        work = Work(task=Task.objects.get(code=self.kwargs.get('code')), user=self.request.user, content=data['content'], created_date=timezone.now())
        work.save()
        return super(OneTask, self).form_valid(form)

    def get_success_url(self):
        return reverse('OneTask', kwargs={'code': self.kwargs.get('code')})

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return self.get(request, *args, **kwargs)
        else:
            return redirect("Login")
