from .models import Book
from django.forms import ModelForm, Textarea
from django.utils.translation import gettext_lazy as _


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'date', 'publisher', 'isbn']
        labels = {
            'title': _('Введите название книги'),
            'author': _('Введите автора'),
            'date': _('Введите дату'),
            'publisher': _('Введите издание'),
            'isbn': _('Введите isbn'),
        }
        help_texts = {
            'text': _('Есть идеи? Пиши'),
            'group': _('Кто ты?')
        }
        widgets = {
            'title': Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'Введите название'}),
        }
        error_massages = {'title': {'required': _('Заполните название')}}
