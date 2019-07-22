from django.conf.urls import url
from user_registration import views as app1_views
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import TemplateView

from user_registration.views import index

urlpatterns = [
    # url(r'^login/$', views.LoginView, name='login'),
    # url(r'^login/$', auth_views.login, {'template_name': 'core/login.html'}, name='login'),
    # url(r'^logout/$', views.LogoutView, name='logout'),
    # url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    # url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='app1/index.html'), name='home'),
    path('login/', auth_views.LoginView, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.LogoutView, {'template_name': 'logged_out.html'}, name='logout'),
    # url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    # url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    # url(r'^signup/$', app1_views.signup, name='signup'),
    path('', index, name='index'),

]
