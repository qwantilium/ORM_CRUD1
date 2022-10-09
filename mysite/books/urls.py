from django.urls import path

from . import views

urlpatterns = [
    path('', views.new_book, name='new_book'),
    path('list/', views.book_list, name='book_list'),
]
