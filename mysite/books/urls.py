from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('', views.new_book, name='new_book'),
    path('<int:id>/', views.book_update, name='book_update'),
    path('delete/<int:id>/', views.book_delete, name='book_delete'),
    path('list/', views.book_list, name='book_list'),
]
