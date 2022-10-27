from django.urls import path
from .views import HomeCheck, Login, Register

urlpatterns = [
    path('', HomeCheck.as_view(), name='Home'),
    path('login/', Login.as_view(), name='Login'),
    path('register/', Register.as_view(), name='Register')
]