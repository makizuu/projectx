from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from .models import Book, Author, Genre
from django.forms import ModelForm
from django.core import serializers
from django.contrib.auth.models import User
from django.utils.timezone import now, timedelta
from itertools import count

import json

# Create your views here.


def index(request):
    search = request.GET.get("search", "")
    borrowed_books = Book.objects.exclude(borrower__isnull=True)
    borrowed_books = borrowed_books.filter(borrower=request.user.pk)
    if search != "":
        all_books2 = Book.objects(pub_date__lte=timezone.now())
        all_books2.objects.filter(title=search).order_by("title")
    else:
        all_books2 = Book.objects.filter(pub_date__lte=timezone.now()).order_by("title")
    context = {"all_books": all_books2, "borrowed_books": borrowed_books}
    return render(request, "library/index.html", context)


class IndexView(generic.ListView):
    template_name = "library/index.html"
    context_object_name = "all_books"

    def get_queryset(self):
        return Book.objects.filter(pub_date__lte=timezone.now()).order_by("title")


def searchresults(request):
    s = request.POST["s"]
    choice = request.POST.get("choice")
    if choice == "a":
        book_list = Book.objects.filter(authors__first_name__icontains=s)
    else:
        book_list = Book.objects.filter(title__icontains=s)

    context = {
        "book_list": book_list,
        "choice": choice,
        "s": s,
    }
    return render(request, "library/searchResults.html", context)


def borrow(request, id):
    # Disallow borrowing a book that is already borrowed.
    user_id = request.user.pk
    user = User.objects.get(pk=user_id)
    book = Book.objects.get(pk=id)
    alreadyBorrowed = book.borrower
    timeSinceLastBorrow = book.days_until_borrow_expires
    # If the book has been borrowed for more than 14 days
    if alreadyBorrowed and timeSinceLastBorrow > 14:
        book.borrower = user
        book.borrowed_at = now()
        book.save()
        return redirect("/library")
    if alreadyBorrowed:
        return HttpResponse("Book is already borrowed")

    book.borrower = user
    book.borrowed_at = now()
    book.save()
    return redirect("/library")


def unborrow(request, id):
    user_id = request.user.pk
    user = User.objects.get(pk=user_id)
    book = Book.objects.filter(pk=id, borrower=user).first()
    book.borrower = None
    book.borrowed_at = None
    book.save()
    return redirect("/library")
