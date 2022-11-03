from django.urls import path
from .views import HomeCheck, Login, Register, OneCourse, OneTask

urlpatterns = [
    path('', HomeCheck.as_view(), name='Home'),
    path('login/', Login.as_view(), name='Login'),
    path('register/', Register.as_view(), name='Register'),
    path('course/<str:code>', OneCourse.as_view(), name="OneCourse"),
    path('task/<str:code>', OneTask.as_view(), name="OneTask")
]