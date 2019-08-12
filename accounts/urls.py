from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    url(r'^register/$', views.register, name='register'),
]
