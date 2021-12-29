from django import forms

from .models import (
    Book,
    Client,
    BookStatus,
    BOOK_STATUS_AVAILABLE,
    BOOK_STATUS_TAKEN,
    expiry
)


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = (
            "name",
            "phone_number"
        )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            "book_name",
            "author",
            "isbn"
        )


class GiveBookForm(forms.ModelForm):
    class Meta:
        model = BookStatus
        fields = (
            "reader",
            "book",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Show only available books
        self.fields["book"].queryset = Book.objects.filter(
            book_status=BOOK_STATUS_AVAILABLE
        )

    def save(self, commit=True):
        book: Book = self.cleaned_data.get("book")
        book.book_status = BOOK_STATUS_TAKEN
        book.save()

        return super().save(commit)


class TakeBookBackForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.filter(
        book_status=BOOK_STATUS_TAKEN
    ))

    def save(self) -> Book:
        book: Book = self.cleaned_data.get("book")
        book.book_status = BOOK_STATUS_AVAILABLE
        book.book_grab.delete()
        book.save()

        return book


class ResetExpiryForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.filter(
        book_status=BOOK_STATUS_TAKEN
    ))

    def save(self) -> Book:
        book: Book = self.cleaned_data.get("book")
        book.book_grab.expiry_date = expiry()
        book.book_grab.save()
        return book
