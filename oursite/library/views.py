from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import Book, Author, Genre
from django.forms import ModelForm
import json

#Create your views here.

def index(request):
    title = ''
    titles = []
    if 'title' in request.GET:
        title = request.GET['title']
        if len(word)>0:
            titles = Dictionary.objects.filter(
                title__icontains=title).order_by('title')
    context = {"titles": titles}
    return render(request, 'library/index.html', context)

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

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title','title']

def search(request):
    def_list = [];
    if 'title' in request.GET:
        titles = request.GET['title']
        if len(title)>0:
            titles = Dictionary.objects.filter(title__icontains=title)
            def_list = [str(title) for title in titles]
    def_json = json.dumps(def_list)
    return JsonResponse(def_json, safe=False)