from django.urls import path

from curriculum.views import index, about, awards

urlpatterns = [

    path('', index, name='index'),
    path('about', about, name='about'),
    #path('experience', experience, name='experience'),
    path('awards', awards, name='awards'),


]
