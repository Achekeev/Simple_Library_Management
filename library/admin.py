from django.contrib import admin
from .models import Book, Client, BookStatus

admin.site.register(Book)
admin.site.register(Client)
admin.site.register(BookStatus)
