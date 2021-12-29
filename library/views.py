from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import (
    ClientForm,
    BookForm,
    GiveBookForm,
    TakeBookBackForm,
    ResetExpiryForm
)
from .models import Book


def index(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'index.html', context)


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


class AddReaderView(View):
    def get(self, request):
        return render(request, 'add_reader.html')

    def post(self, request):
        form = ClientForm(request.POST)

        if form.is_valid():
            form.save()
            context = {
                "alert": True
            }
            return render(request, 'add_reader.html', context)

        context = {
            "form": form
        }
        return render(request, 'add_reader.html', context)


class AddBookView(View):
    def get(self, request):
        return render(request, 'add_book.html')

    def post(self, request):
        form = BookForm(request.POST)

        if (form.is_valid()):
            form.save()
            context = {
                "alert": True
            }
            return render(request, 'add_book.html', context)

        context = {
            "form": form
        }
        return render(request, 'add_book.html', context)


class GiveBookView(View):
    def get(self, request):
        form = GiveBookForm()
        context = {
            "form": form
        }
        return render(request, "give_book.html", context)

    def post(self, request: HttpRequest):
        form = GiveBookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse("Main_Page"))

        context = {
            "form": form
        }
        return render(request, "give_book.html", context)


class TakeBookBackView(View):
    def get(self, request):
        form = TakeBookBackForm()
        context = {
            "form": form
        }
        return render(request, "take_book_back.html", context)

    def post(self, request):
        form = TakeBookBackForm(request.POST)
        context = {
            "form": form
        }

        if form.is_valid():
            print("Valid!")
            form.save()
            return redirect(reverse("give_book"))

        return render(request, "take_book_back.html", context)


class ResetExpiryView(View):
    def get(self, request):
        permitted_methods = (
            "GET",
        )
        return HttpResponseNotAllowed(permitted_methods=permitted_methods)

    def post(self, request, pk=None):
        form = ResetExpiryForm({"book": pk})

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(redirect_to=reverse("Main_Page"), )

        errors_string = ' '.join(form.errors.values())
        return HttpResponse(f"Invalid form, "
                            f"couldn't reset expiry, "
                            f"these are errors {errors_string}")
