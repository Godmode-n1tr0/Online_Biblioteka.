from django.views import generic
from django.shortcuts import render

# Create your views here.

from .models import Book, Genre, Author

def index(request):
    count_books=Book.objects.all().count()
    count_author=Author.objects.all().count()
    return render(request, 'index.html', context={'count_books': count_books, 'count_author': count_author})

class BookViews(generic.ListView):
    model = Book
