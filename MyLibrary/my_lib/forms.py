from django import forms
from .models import Books


class BooksForm(forms.ModelForm):
    new_author_name = forms.CharField(max_length=100, required=False, label='Name')
    new_author_lastname = forms.CharField(max_length=100, required=False, label='Lastname')
    new_series = forms.CharField(max_length=100, required=False, label='New Series')


    class Meta:
        model = Books
        fields = '__all__'
        labels = {
            'title': 'Book Title',
            'author': 'Author',
            'series': 'Series',
            'read': 'Read?',
            'bought': 'Bought?'
        }

