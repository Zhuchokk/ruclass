from django.urls import path, include
from .views import Home, Login, Register, OneCourse, OneTask

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('login/', Login.as_view(), name='Login'),
    path('register/', Register.as_view(), name='Register'),
    path('course/<str:code>', OneCourse.as_view(), name="OneCourse"),
    path('task/<str:code>', OneTask.as_view(), name="OneTask"),
    path('summernote/', include('django_summernote.urls')),
]