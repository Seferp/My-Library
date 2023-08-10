from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, DeleteView
from django.urls import reverse_lazy
from .models import Books, Authors, Series
from .forms import BooksForm

# Create your views here.


class Home(View):
    def get_books(self):
        books = Books.objects.filter(bought=True).order_by('id')
        for book in books:
            if book.read == True:
                book.read_display = 'Read'
            else:
                book.read_display = 'Unread'
        return books

    def get_planed_books(self):
        planed_books = Books.objects.filter(bought=False).order_by('id')
        return planed_books


    def get(self, request):
        books = self.get_books()
        form = BooksForm()
        planed_books = self.get_planed_books()

        context = {
            'books': books,
            'form': form,
            'planed_books': planed_books
        }
        return render(request, 'my_lib/home.html', context)


    def post(self, request):
        form = BooksForm(request.POST)

        if form.is_valid():
            new_author_name = form.cleaned_data.get('new_author_name')
            new_author_lastname = form.cleaned_data.get('new_author_last_name')
            new_series_name = form.cleaned_data.get('new_series')

            if new_author_name or new_author_lastname:
                new_author = Authors.objects.create(name=new_author_name, lastname=new_author_lastname)
                book = form.save(commit=False)
                book.author = new_author

                if new_series_name:
                    new_series = Series.objects.create(name=new_series_name)
                    book.series = new_series

                book.save()

            else:
                if new_series_name:
                    new_series = Series.objects.create(name=new_series_name)
                    book = form.save(commit=False)
                    book.series = new_series

                form.save()

            return redirect('home')
        else:
            books = self.get_books()

        context = {
            'books': books,
            'form': form,
        }
        return render(request, 'my_lib/home.html', context)



class DeleteBook(DeleteView):
    model = Books
    success_url = reverse_lazy('home')

    def delete_book(self, book_id):
        book_delete = get_object_or_404(Books, id=book_id)
        book_delete.delete()
        return redirect('home')

class UpdateBook(View):
    model = Books
    template_name = 'my_lib/home.html'
    success_url = reverse_lazy('home')

    def get(self, request, book_id):
        book = get_object_or_404(Books, id=book_id)
        return render(request, self.template_name, {'book': book})
    def post(self, request, book_id):
        book = get_object_or_404(Books, id=book_id)
        fields_to_update = request.POST.getlist('fields_to_update')

        if 'read' in fields_to_update:
            book.read = not book.read
        if 'bought' in fields_to_update:
            book.bought = not book.bought

        book.save()
        return redirect('home')
