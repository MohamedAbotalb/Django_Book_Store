from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse

import json

from books.models import Book

books = [
    {
        "title": "The C Programming Language",
        "author": "John Doe",
        "price": 280,
        "pages": 250,
        "img": "1.jpg",
        "id": 1
    },
    {
        "title": "Eloquent JavaScript",
        "author": "John Doe",
        "price": 120,
        "pages": 30,
        "img": "2.png",
        "id": 2
    },
    {
        "title": "The Complete Book on Angular",
        "author": "John Doe",
        "price": 100,
        "pages": 550,
        "img": "3.jpg",
        "id": 3
    },
    {
        "title": "Head First Java",
        "author": "John Doe",
        "price": 150,
        "pages": 400,
        "img": "4.jpg",
        "id": 4
    },
    {
        "title": "Node.js in Action",
        "author": "John Doe",
        "price": 200,
        "pages": 320,
        "img": "5.png",
        "id": 5
    },
    {
        "title": "Full Stack React",
        "author": "John Doe",
        "price": 140,
        "pages": 350,
        "img": "6.jpg",
        "id": 6
    },
    {
        "title": "Vue.js in Action",
        "author": "John Doe",
        "price": 180,
        "pages": 45,
        "img": "7.jpg",
        "id": 7
    },
    {
        "title": "Programming Python",
        "author": "John Doe",
        "price": 220,
        "pages": 380,
        "img": "8.jpg",
        "id": 8
    },
    {
        "title": "C# in a Nutshell",
        "author": "John Doe",
        "price": 300,
        "pages": 950,
        "img": "9.jpg",
        "id": 9
    }
]


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def home(request):
    return render(request, 'books/home.html', context={"books": books}, status=200)


def book_details(request, book_id):
    filtered_books = filter(lambda book: book['id'] == book_id, books)
    filtered_books = list(filtered_books)
    if filtered_books:
        book = filtered_books[0]
        return render(request, 'books/book_details.html', context={"book": book}, status=200)
    return HttpResponse("No book found with that id")


def about(request):
    return render(request, 'books/about.html', status=200)


def contact(request):
    return render(request, 'books/contact.html', status=200)


def books_index(request):
    books = Book.objects.all()
    return render(request, "books/crud/index.html", context={"books": books})


def book_show(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "books/crud/show.html", context={"book": book})


def book_delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    url = reverse("index_page")
    return redirect(url)


def book_create(request):
    if request.method == "POST":
        image = "books/images/default.png"
        if request.FILES:
            image = request.FILES["image"]

        book = Book(title=request.POST["title"], author=request.POST["author"], price=request.POST["price"],
                    pages=request.POST["pages"], image=image)
        book.save()
        return redirect(book.show_url)

    return render(request, 'books/crud/create.html')


def book_update(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":
        image = book.image
        if request.FILES:
            image = request.FILES["image"]

        book.title = request.POST["title"]
        book.author = request.POST["author"]
        book.price = request.POST["price"]
        book.pages = request.POST["pages"]
        book.image = image
        book.save()

        return redirect("book_show", book_id=book_id)

    return render(request, "books/crud/update.html", {"book": book})
