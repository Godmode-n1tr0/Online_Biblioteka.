# from django import views
from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookViews.as_view(), name='books'),
    path('book/<int:pk>', views.BookAllView.as_view(), name='book-detail'),
    path('author/', views.Authorlist.as_view(), name='author'),
    path('author/<int:pk>', views.BookAllView.as_view(), name='author-detail')
]
