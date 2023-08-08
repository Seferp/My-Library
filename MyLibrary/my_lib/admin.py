from django.contrib import admin
from .models import Authors, Series, Books

# Register your models here.

class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname')


class SeriesAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BooksAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Books, BooksAdmin)