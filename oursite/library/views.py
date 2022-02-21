from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.urls import reverse_lazy
from .models import Book, Author, Genre

#Create your views here.
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

class IndexView(generic.ListView):
    template_name = 'library/index.html'
    context_object_name = 'latest_books'
    def get_queryset(self):
        return Book.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
