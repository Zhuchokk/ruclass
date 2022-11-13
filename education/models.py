from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', default=User.objects.get(id=1).pk)
    members = models.ManyToManyField(User, related_name='members')
    code = models.CharField('Код курса', max_length=10, unique=True)
    description = models.CharField('Описание курса', max_length=300)
    name = models.CharField('Название курса', max_length=100)


class Task(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    code = models.CharField('Код курса', max_length=10, unique=True)
    title = models.CharField('Название задания', max_length=300)
    instructions = models.TextField('Инструкции')
    deadline = models.DateTimeField('Срок сдачи')
    created_date = models.DateTimeField('Дата назначения')
    points = models.IntegerField('Баллы', default=5)
    #homeworks


class Work(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.IntegerField('Оценка', default=5)
    content = models.TextField('content')
    created_date = models.DateTimeField('Дата сдачи')