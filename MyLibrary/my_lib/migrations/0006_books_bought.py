# Generated by Django 4.2.4 on 2023-08-10 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_lib', '0005_delete_planedbooks'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='bought',
            field=models.BooleanField(default=False, verbose_name=[(True, 'Yes'), (False, 'No')]),
            preserve_default=False,
        ),
    ]
