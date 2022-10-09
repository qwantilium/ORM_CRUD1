from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'publisher', 'isbn',)
    search_fields = ("title",)
    list_filter = ("author",)
    empty_value_display = "-пусто-"


admin.site.register(Book, BookAdmin)
