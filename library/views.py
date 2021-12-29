from django.shortcuts import render
from .models import Book, Client, BookStatus
from django.views import generic


def index(request):
    return render(request, 'index.html')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def add_reader(request):
    if request.method == "POST":
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        reader = Client.objects.create(name=name, phone_number=phone_number)
        reader.save()
        alert = True
        return render(request, 'add_reader.html', {'alert': alert})
    return render(request, 'add_reader.html')


def add_book(request):
    if request.method == 'POST':
        book_name = request.POST['book_name']
        author = request.POST['author']
        isbn = request.POST['isbn']
        book_status = 'Доступна'
        books = Book.objects.get_or_create(book_name=book_name, author=author, isbn=isbn, book_status=book_status)
        books.save()
        alert = True
        return render(request, 'add_book.html', {'alert': alert})
    return render(request, 'add_book.html')


