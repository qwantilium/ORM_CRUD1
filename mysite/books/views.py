from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def new_book(request):
    form = BookForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        data = form.save(commit=False)
        data.author = user
        data.save()
        return redirect('index')
    return render(request, 'books/new_book.html', {'form': form})


def book_list(request):
    latest = Book.objects.filter
    return render(request, "books/book_list.html", {"books": latest})
