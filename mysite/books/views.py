from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def new_book(request):
    form = BookForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save(commit=False)
        return redirect('book_list')
    return render(request, 'new_book.html', {'form': form})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})
