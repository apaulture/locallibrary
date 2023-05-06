from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import *

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,

        # Challenge 5.2
        'action_genres': Genre.objects.filter(name__icontains = 'action').count(),
        'dark_books': Book.objects.filter(title__icontains = 'dark').count()
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(ListView):
    model = Book
    # template = 'books.html' # default but can be overridden by passing specified template in pattern

    # def get_queryset(self):
        # use case: filter based on title and number of books to show
        # return Book.objects.filter(title__icontains='flower')[:5]
    
    def get_context_data(self, **kwargs):
        # Grab existing context from superclass (ListView)
        context = super().get_context_data(**kwargs) # see inheritance-practice.py
        print(context)
        return context

class BookDetailView(DetailView):
    model = Book