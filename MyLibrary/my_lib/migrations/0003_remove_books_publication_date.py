# Generated by Django 4.2.4 on 2023-08-09 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_lib', '0002_alter_books_author_alter_books_publication_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='publication_date',
        ),
    ]