from django.db import models

# Create your models here.


class Authors(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.lastname}'


class Series(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Books(models.Model):
    yes_or_no_choices = [(True, 'Yes'), (False, 'No')]

    title = models.CharField(max_length=100, blank=False)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, null=True, blank=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, null=True, blank=True)
    read = models.BooleanField(yes_or_no_choices)
    bought = models.BooleanField(yes_or_no_choices)

    def __str__(self):
        return f'{self.title}'
