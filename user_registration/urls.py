from django.conf.urls import url
from django.contrib.auth import views
from django.urls import path
from django.views.generic.base import TemplateView

from user_registration.views import index

urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name='app1/index.html'), name='home'),
    path('', index, name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password_reset_email/',views.PasswordResetView.as_view(),name='password_reset_mail'),
    path('password_reset_done/',views.PasswordResetDoneView.as_view(),name='passsword_reset_done'),
    path('password_reset_confirm/',views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_complete/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
