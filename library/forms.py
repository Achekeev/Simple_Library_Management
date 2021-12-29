from django import forms
from .models import Book, Client, BookStatus


class GiveBookForm(forms.Form):
    book_name = forms.MultipleChoiceField(queryset=Book.objects.all())
    reader = forms.MultipleChoiceField(queryset=Client.objects.all())
    book_status = forms.ModelChoiceField(queryset=Book.objects.get(book_status), empty_label="Доступна")
    status_create = BookStatus.objects.create(book_name=book_name, reader=reader, book_status=book_status)
    status_create.save()



