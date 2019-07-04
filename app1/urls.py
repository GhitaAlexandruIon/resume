from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import TemplateView

from app1.views import index

urlpatterns = [
    # url(r'^login/$', views.LoginView, name='login'),
    # url(r'^login/$', auth_views.login, {'template_name': 'core/login.html'}, name='login'),
    # url(r'^logout/$', views.LogoutView, name='logout'),
    # url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    # url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='app1/index.html'), name='home'),
    url(r'^login/$', auth_views.LoginView, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.LogoutView, {'template_name': 'logged_out.html'}, name='logout'),
    path('', index, name='index'),

]
