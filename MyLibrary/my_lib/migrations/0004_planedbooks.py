# Generated by Django 4.2.4 on 2023-08-09 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_lib', '0003_remove_books_publication_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanedBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_lib.authors')),
                ('series', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_lib.series')),
            ],
        ),
    ]
