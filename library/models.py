from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField("year published")
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)
    borrower = models.ForeignKey(
        User,
        related_name="borrower",
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
    )
    borrowed_at = models.DateField(null=True, blank=True)

    def days_until_borrow_expires(self):
        borrowed_at = self.borrowed_at or now()
        delta = now() - borrowed_at
        return delta.days()
