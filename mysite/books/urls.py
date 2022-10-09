from django.urls import path

from . import views

urlpatterns = [
    path('', views.book_list, name='new_book'),
    path('book_list/', views.new_book, name='book_list'),
]
