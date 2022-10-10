from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm


def new_book(request):
    # Create
    title = 'Добавить книгу'
    button = 'Добавить'
    form = BookForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = form.save(commit=False)
        data.save()
        return redirect('books:book_list')
    return render(request, 'new_book.html', {'form': form, 'title': title, 'button': button})


def book_list(request):
    # Read
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def book_update(request, id):
    # Update
    title = 'Редактировать запись c ISBN'
    button = 'Редактировать'
    book = get_object_or_404(Book, id=id)
    form = BookForm(
        request.POST or None, files=request.FILES or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('books:book_list')
    return render(
        request, 'new_book.html',
        {'form': form, 'title': title, 'button': button, 'book': book},
    )


def book_delete(request, id):
    # delete
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('books:book_list')
