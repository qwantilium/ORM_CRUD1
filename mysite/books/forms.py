from .models import Book
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'date', 'publisher', 'isbn']
        labels = {
            'title': _('Введите название книги'),
            'author': _('Введите автора'),
            'date': _('Введите год'),
            'publisher': _('Введите издание'),
            'isbn': _('Введите isbn'),
        }
        error_massages = {'title': {'required': _('Заполните название')}}
