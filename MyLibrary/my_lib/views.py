from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Books
# Create your views here.


class Home(View):
    def get_books(self):
        books = Books.objects.all().order_by('id')
        for book in books:
            if book.read == True:
                book.read_display = 'Tak'
            else:
                book.read_display = 'Nie'
        return books

    def get(self, request):
        books = self.get_books()

        context = {
            'books': books
        }
        return render(request, 'my_lib/home.html', context)
