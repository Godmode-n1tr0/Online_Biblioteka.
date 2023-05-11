# from django import views
from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('^books/$', views.BookViews.as_view(), name='books')
]