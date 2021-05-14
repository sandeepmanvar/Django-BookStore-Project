from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg
# Create your views here.


def index(request):
    books = Book.objects.all().order_by("-rating")
    total_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_books": total_books,
        "avg_rating": avg_rating
    })


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book-detail.html", {"book": book})
