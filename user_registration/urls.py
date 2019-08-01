from django.conf.urls import url
from django.contrib.auth import views
from django.urls import path
from django.views.generic.base import TemplateView

from user_registration.views import index

urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name='app1/index.html'), name='home'),
    path('', index, name='index'),
    path('login/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    # path('signup/',  views.SignupView.as_view(template_name='registration/signup.html'),name='signup'),
    # path('password_reset_form/', views.SetPasswordForm.as_view(template_name='password_reset_form.html'),
    # name='password_reset_form'),
    path('password_reset_email/',
         views.PasswordResetView.as_view(template_name='registration/password_reset_email.html'),
         name='password_reset_mail'),
    path('password_reset_done/',
         views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='passsword_reset_done'),
    path('password_reset_confirm/',
         views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/',

         views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complate'),
    #path('signup/', views.Sign.as_view(), name='signup'),

]
