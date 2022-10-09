from django.urls import path

from . import views

urlpatterns = [
    path('book_list', views.book_list, name='book_list'),
    path('new_book/', views.new_book, name='new_book'),
]
