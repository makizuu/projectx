from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import Book, Author, Genre, Customer
from django.forms import ModelForm
import json

#Create your views here.

def index(request, book):
    if request.method == 'GET':
        search = request.GET.get('book')
        post = book.objects.all().filter(content__contains=results)
    return render(request, {'post': post})


class CreateBookView(CreateView):
    model = Book
    template_name = 'library/create.html'
    fields = ['title', 'pub_date', 'authors', 'genres']
    success_url = reverse_lazy('library:index')

class UpdateBookView(UpdateView):
    model = Book
    template_name = 'library/update.html'
    fields = ['title', 'pub_date', 'authors', 'genres'] 
    success_url = reverse_lazy('library:index')

class DeleteBookView(DeleteView):
    model = Book
    #template_name =- 'library/delete.html'
    success_url = reverse_lazy('library:index')

#Täytyy tehdä LoanBook & ReturnBook Classit ja poistaa normaalikäyttäjältä Update, Create ja Delete mahdollisuudet.

class IndexView(generic.ListView):
    template_name = 'library/index.html'
    context_object_name = 'all_books'
    def get_queryset(self):
        return Book.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('title')[:10]